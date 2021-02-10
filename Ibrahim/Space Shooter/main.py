import pygame
import os
import time
import random
import time
pygame.font.init()
WIDTH,HEIGHT =750,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Proje")


#foto yükleme
red_SHIP= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_ship_red_small.png"))
blue_SHIP= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_ship_blue_small.png"))
green_SHIP= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_ship_green_small.png"))

#lazerler
red_LASER= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_laser_red.png"))
blue_LASER= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_laser_blue.png"))
green_LASER= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_laser_green.png"))

#ana oyuncu
yellow_SHIP= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_ship_yellow.png"))
yellow_LASER= pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","pixel_laser_yellow.png"))

#arkaplan
bg=pygame.transform.scale((pygame.image.load(os.path.join(r"Ibrahim\Space Shooter\assets","background-black.png"))),(WIDTH,HEIGHT))
class Laser:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,window):
        WIN.blit(self.img,(self.x,self.y))
    
    def move(self,vel):
        self.y+=vel

    def off_screen(self,height):
        return not(self.y < height and self.y >= 0)
    
    def collision(self,obj):
        return collide(self,obj)


#absract class kullanıcaz yani yapı oluşturucazki diğer yerlerde kullanabilelim
class Ship:
    COOLDOWN = 7
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        #gemilerin elementleri
        self.ship_img= None
        self.laser_img= None
        self.lasers= []
        self.cool_down_counter= 0

    #gemileri çizdiriyorz

    def draw(self,WIN):
        WIN.blit(self.ship_img,(self.x,self.y))
        for laser in self.lasers:
            laser.draw(WIN)

    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -=10
                self.lasers.remove(laser)



    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter=0
        elif self.cool_down_counter >0:
            self.cool_down_counter+=1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter=1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img= yellow_SHIP
        self.laser_img= yellow_LASER
        #unitydeki gibi collider mantığı için maske oluşturuyor ve pixel infosu veriyor
        self.mask=pygame.mask.from_surface(self.ship_img)
        self.max_health=health

    def move_lasers(self,vel,objs):
        self.cooldown()
        try:
            for laser in self.lasers:
                laser.move(vel)
                if laser.off_screen(HEIGHT):
                    self.lasers.remove(laser)
                else:
                    for obj in objs:
                        if laser.collision(obj):
                            objs.remove(obj)
                            self.lasers.remove(laser)
        except:
            pass
    
    def healthbar(self,window):
        pygame.draw.rect(window,(255,0,0),(self.x , self.y + self.ship_img.get_height() +10, self.ship_img.get_width(),10))
        pygame.draw.rect(window,(0,255,0),(self.x , self.y + self.ship_img.get_height() +10, self.ship_img.get_width()*(self.health/self.max_health),10))

    def draw(self,window):
        super().draw(window)
        self.healthbar(window)
class Enemy(Ship):
    #her seferide yazmamak için bir adet renk sözlüğü yazdık ve paket halinde tuple tuttuk
    COLOR_MAP= {"red":(red_SHIP,red_LASER),"blue":(blue_SHIP,blue_LASER),"green":(green_SHIP,green_LASER)}
    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        #sözlükteki renkin karşılığı key value olarak fonksiyondaki değerlere döndü
        self.ship_img , self.laser_img = self.COLOR_MAP[color]
        self.mask=pygame.mask.from_surface(self.ship_img)
    def move(self,vel):
        self.y+=vel
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter=1

def collide(obj1,obj2):
    offset_x=obj2.x - obj1.x
    offset_y=obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None

def main():
    #parametreler
    run = True
    FPS = 60
    level=0
    lives=5
    lost=False
    lost_count=0
    laser_vel=7
    enemylaser_vel=7
    main_font=pygame.font.SysFont("comicsans",30)
    lost_font=pygame.font.SysFont("comicsans",100)
    player_vel=12
    player=Player(300,650)
    enemies=[]
    enemy_vel=4
    wave_length=5


    #verdiğim fps dğerinde çalışmasını sağlıyorum
    clock=pygame.time.Clock()

    #bişeyleri çizdirmem gerekiyor yoksa pencerede gözükmez bu yüzden WIN penceresinde blit fonksiyonunu kullandım ve ekranı güncelledim
    def redraw_window():
        WIN.blit(bg,(0,0))

        #yazı çizme
        level_label=main_font.render(f"Level:{level}",1,(255,255,255))
        lives_label=main_font.render(f"Ship Limit: {lives}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        # WIN.blit(level_label,(675,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))

        for enemy in enemies:
            enemy.draw(WIN)

        
        #gemi çizme
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You Lost!",1,(255,255,255))
            WIN.blit(lost_label,((WIDTH/2 - lost_label.get_width()/2),HEIGHT/2))
        pygame.display.update()
        
    while run:

        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost=True
            lost_count+=1
            main_menu()

        if lost:
            if lost_count > FPS * 3:
                run=False
                main_menu()
            else:
                continue

        if len(enemies) == 0:
            level+=1
            wave_length += 5
            for i in range(wave_length):
                enemy= Enemy(random.randrange(50,WIDTH-100),random.randrange(-1500,-100),random.choice(["red","blue","green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
        #hareket
        #pygame kordinat sistemi 4. bölgededir
        #merkez sol üstte olduğu için çizdirdiğimiz küpün boyutlarını eklersek kenarlardan o boyut kadar uzak duracaktır
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: #sol
            player.x-=player_vel
        if keys[pygame.K_d] and player.x+player_vel +player.get_width() <WIDTH: #sağ
            player.x+=player_vel
        if keys[pygame.K_w]and player.y - player_vel > 0 : #yukarı
            player.y-=player_vel
        if keys[pygame.K_s] and player.y + player_vel +player.get_height() + 20 < HEIGHT: #aşağı
            player.y+=player_vel

        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel),
            enemy.move_lasers(enemylaser_vel,player)

            if random.randrange(0,2*60)==1:
                enemy.shoot()
            
            if collide(enemy, player):
                player.health-=10
                enemies.remove(enemy)
            
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives-=1
                enemies.remove(enemy)

            
        player.move_lasers(-laser_vel,enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        WIN.blit(bg, (0,0))
        title_label = title_font.render("Press mouse to play(or again)", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
    
main_menu()