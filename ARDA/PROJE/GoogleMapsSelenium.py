#----------------------------------------------------------------------------------------

#pip install selenium

#----------------------------------------------------------------------------------------

from selenium import webdriver
from time import sleep
from tkinter import *

#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------

def basla():
    gidilecek = entry_1.get()
    baslangic = entry_2.get()
    tarayici = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
    tarayici.get("https://www.google.ng/maps/@38.95682,35.174414,6z?hl=tr")

   


    sleep(5)


    gidilecek_konum =  tarayici.find_element_by_class_name('tactile-searchbox-input')
    gidilecek_konum.send_keys(gidilecek)

    aramatusu = tarayici.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/button")
    aramatusu.click()

   


    sleep(3)


    baslangic_konum =  tarayici.find_element_by_css_selector('#sb_ifc51 > input:nth-child(1)')
    baslangic_konum.send_keys(baslangic)

    aramatusu2 = tarayici.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    aramatusu2.click()


    sleep(5)


    toplamkilometre = tarayici.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]/div")
    araba_zaman = tarayici.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]")
    
    km = toplamkilometre.text
    araba = araba_zaman.text
    ekranayaz = km
    ekranayaz1 = araba
    label_3 = Label(my_window)
    label_3["text"]=ekranayaz
    label_3.grid(row=3, column=2)
    label_4 = Label(my_window)
    label_4["text"]=ekranayaz1
    label_4.grid(row=4, column=2)



my_window = Tk()

#----------------------------------------------------------------------------------------


label_1 = Label(my_window,text="Başlangıç Konumu")
label_2 = Label(my_window,text="Hedef Konum")
label_5 = Label(my_window,text="Toplam Mesafe : ")
label_6 = Label(my_window,text="Araba İle Zaman : ")
entry_1 = Entry(my_window)
entry_2 = Entry(my_window)
button_1 = Button(my_window,text="Başlat",command=basla)


label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0)
label_5.grid(row=3, column=1)
label_6.grid(row=4, column=1)
entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
button_1.grid(row=3, column=0)


#----------------------------------------------------------------------------------------

my_window.mainloop()


