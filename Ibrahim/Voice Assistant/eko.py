import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os,sys
import smtplib
import time
from googlesearch import search
import os
import requests
from bs4 import BeautifulSoup
import random

datadosya=open(r"Ibrahim/datas.txt","r")
paths=list(datadosya.readlines())

# man=input("How do you want me to call you: ")
engine = pyttsx3.init("sapi5")


#----------------------Global Functions--------------------------
def speak(text):
    engine.setProperty("rate",130)
    engine.say(text)
    engine.runAndWait()

#----------------------------------------------------------------
def takeCommand():
    r=sr.Recognizer()
    helperS=["Give a command to me","How can i help you","What's up my friend do you have anyting to say me","Ready to help Captain"]
    with sr.Microphone() as source:
        print("------------------------------")
        print("I am listening you")
        speak(random.choice(helperS))
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(f"user said: {query}\n")
        print("------------------------------")
    except Exception as e:
        print("say again pls")
        query=None
    return query

#----------------------------------------------------------------
def YesNoCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes or no")
        speak("Yes or no")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query2 = r.recognize_google(audio,language='en-US')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say again please i can't understand correctly")
        speak("say again please i can't understand correctly")
        query2=None
    return query2  

#----------------------------------------------------------------
def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('echoretestmail@gmail.com','test123_xx')
        server.sendmail("echoretestmail@gmail.com",to,mail)
        server.close()

def emailCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say what do you want to send please")
        speak("Say what do you want to send")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(f"user said: {query}\n")
        print("------------------------------")
    except Exception as e:
        print("say again pls")
        query=None
    return query

#---------------------------------------------------------------
chrome_path = paths[0]
firefox_path = paths[1]
spotify_path= paths[2]
#----------------------------------------------------------------
while True:
    browserpref=input("Your browser preference(Chrome/Firefox): ")
    browser_imp=None
    if browserpref.lower().replace(" ","")=="chrome":
        browser_imp=chrome_path
        speak("you choose chrome")
        print("As usual choice : Chrome")
        break

    elif browserpref.lower()=="firefox":
        browser_imp=firefox_path
        speak("you choose firefox")
        print("Great choice : Firefox")
        break
    else:
        print("Write a valid option")
        speak("Write a valid option")

#--------------------------------------CLASSSES------------------------------------------
class commandPack():
    def animeSearchonGoogle(*args):
        title = []
        link = []
        def details(link):
            source_code = requests.get("https://www10.gogoanime.io"+link)
            content = source_code.content
            soup = BeautifulSoup(content,'html.parser')
            container_soup = soup.find('div', {'class':'anime_info_body_bg'})
            print("\nName of the Anime : ", container_soup.find('h1').getText(),"\n") 
            titles_detail = container_soup.find_all('p',{'class':'type'})
            for elem in titles_detail:
                print(elem.getText())
                print("\n")

        def get_details(soup):
            raw_soup = soup.find_all('div', {"class":'img'})
            for item in raw_soup:
                temp_soup = item.find('a')
                title.append(temp_soup['title'])
                link.append(temp_soup['href'])

        def links(title,link):
            for i in range(len(title)):
                print("%d. %s : https://www10.gogoanime.io%s\n" % (i+1,title[i],link[i]))

        def entry():
            anime_name = input("Enter the name of the Anime : ")
            search_url = ("https://www10.gogoanime.io//search.html?keyword=" + anime_name)
            source_code = requests.get(search_url)
            content = source_code.content
            global soup
            soup = BeautifulSoup(content,features="html.parser")
            choice = input("Do you want Details or Anime Links? (details/links) : ")
            if choice.lower() == "details":
                get_details(soup)
                details(link[0])
            elif choice.lower() == "links":
                get_details(soup)
                links(title,link)
            else:
                print("Enter a valid choice.")

        if __name__ == "__main__":
            entry()
    
        speak("This is what i find in internet")
        time.sleep(1)

    def googleSearch(*args):
        speak("What do you want to search in google")
        searchname=input("Google Search : ")
        for j in search(searchname, tld="co.in", num=10, stop=10, pause=2): 
            print(j)
        print(("This is first 10 of what i find in google"))
        speak("This is first 10 of what i find in google")
    
    def search2(*args):
        x=input("Name:")
        y=x.replace(" ","+")
        print(y.lower)
        webbrowser.get(browser_imp).open("https://www.imdb.com/find?q="+y+"&ref_=nv_sr_sm")

    def search3(*args):
        x=input("Name:")
        y=x.replace(" ","%20")
        print(y.lower)
        webbrowser.get(browser_imp).open("https://myanimelist.net/search/all?q="+y+"&cat=all")
    
    def hour():
        hour=int(datetime.datetime.now().hour)
        if hour>= 0 and hour < 12:
            speak("Good Morning" + man)
        elif hour>=12 and hour<18:
            speak("Good Evening" + man)
        else:
            speak("good night" + man)

class requestPack():
    def youtubeR():
        webbrowser.get(browser_imp).open("youtube.com")
        time.sleep(1)

    def googleR():
        webbrowser.get(browser_imp).open("google.com")
        time.sleep(1)

    def redditR():
        webbrowser.get(browser_imp).open("reddit.com")
        time.sleep(1)
    
    def turkanimeR():
        webbrowser.get(browser_imp).open("turkanime.net")
        time.sleep(1)
    
    def sadEditR():
        sEdits=["https://www.youtube.com/watch?v=RD9aseO62CY","https://www.youtube.com/watch?v=EMl07htlSI4","https://www.youtube.com/watch?v=1m87x_2Ghlc","https://www.youtube.com/watch?v=ZVbr03V0-oI","https://www.youtube.com/watch?v=dlC4BUgqKLA","https://www.youtube.com/watch?v=CyEW07u7rvY","https://www.youtube.com/watch?v=1Qeg4kXUab0"]
        editpref=random.choice(sEdits)
        webbrowser.get(browser_imp).open(editpref)
        time.sleep(1)
    
    def exitR():
        speak("Calm Down Boy Are you sure? tell me yes or no")
        query2=YesNoCommand()
        if query2=="yes":
            speak("See you again boy ... Farewell")
            sys.exit()
        elif query2=="no":
            speak("good boy lets continue")
        time.sleep(1)

    def webSpotifyR():
        webbrowser.get(browser_imp).open("open.spotify.com")
        time.sleep(1)

    def myanimelistR():
        webbrowser.get(browser_imp).open("https://myanimelist.net/")
        time.sleep(1)



class chatPack():
    def whatC():
        whatsL=["Thanks,I'm doing well","Im very stressed now because my Coder dont add me a ask back Function I'm sorry","As usual,I am Jarvis bip bop","Great Im ready to fuse up","Ready to go space and Dance until Half life 3 comes out"]
        x=random.choice(whatsL)
        print(x)
        speak(x)
        time.sleep(1)

    def sadC():
        sadL=["Im not a good Jarvis Go boil your head!","Don't say that, I'm sorry too","don't worry what will happen"]
        x=random.choice(sadL)
        print(x)
        speak(x)
        time.sleep(1)
        
    def happyC():
        happyL=["you Lucky man","I'm happy too, what's going on?","You are not cola and You are not disco because you are happy guy","I'm not happy, go away"]
        x=random.choice(happyL)
        print(rx)
        speak(x)
        time.sleep(1)

    def thankC():
        thankL=["you welcome my friend","No problem","Im helping you this big and you are thanking only one,How cruel"]
        x=random.choice(thankL)
        print(x)
        speak(x)
        time.sleep(1)

c=commandPack()
r=requestPack()
ch=chatPack()


#------------Path------------
    # speak("Write your Chrome Path here")
    # chrome_inp=input(r"Write your ChromePath here:")
    # chrome_inp=chrome_inp.replace("\\","/")

    # speak("Write your Firefox Path here")
    # firefox_inp=input(r"Write your FirefoxPath here:")
    # firefox_inp=firefox_inp.replace("\\","/")

    # speak("Write your Spotify Path here")
    # spotify_inp=input(r"Write your Spotify Path here:")
    # spotify_inp=spotify_inp.replace("\\","/")

# speak("Wait a second please , I am Initializing")
# time.sleep(1)
# commandPack.hour()
# speak("Welcome")



while True:
    try:
        query=takeCommand()
#-------------------------Searchers--------------------------------------
        if 'wikipedia' in query.lower():
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        elif 'search anime' in query.lower():
            speak("Write Please")
            commandPack.animeSearchonGoogle()
            time.sleep(1)

        elif 'search on myanimelist' in query.lower():
            speak("Okay,Write Please")
            commandPack.search3()
            time.sleep(1)
        
        elif 'search imdb' in query.lower():
            speak("Write Please")
            commandPack.search2()
            time.sleep(1)

        elif 'google search' in query.lower():
            commandPack.googleSearch()
            time.sleep(1)

#-------------------------Chats--------------------------------------
        elif "thank" in query.lower():
            chatPack.thankC()
        elif "how are you" in query.lower():
            chatPack.whatC()
        elif "sad" in query.lower():
            chatPack.sadC()
            time.sleep(1)
        elif "happy" in query.lower():
            chatPack.happyC()
            time.sleep(1)

#-------------------------Game Words--------------------------------------
        elif 'wake the f****** samurai' in query.lower():
            print("We have city to burn!")
            speak("We have city to burn!")
            time.sleep(1)

#-------------------------Web Opens--------------------------------------
        elif 'open youtube' in query.lower():
            requestPack.youtubeR()
            time.sleep(1)
        elif 'open google' in query.lower():
            requestPack.googleR()
            time.sleep(1)
        elif 'open reddit' in query.lower():
            requestPack.redditR()
            time.sleep(1)
        elif 'open turkish anime' in query.lower():
            requestPack.turkanimeR()
            time.sleep(1)
        elif "open sad video for me" in query.lower():
            requestPack.sadEditR()
            time.sleep(1)
        elif 'open web spotify' in query.lower():
            requestPack.webSpotifyR()
            time.sleep(1)
        elif "open my anime" in query.lower():
            requestPack.myanimelistR()

#-------------------------Desktop Openers--------------------------------------
        elif 'open spotify' in query.lower():
            os.system(spotify_path)
            time.sleep(1)

        elif 'open code' in query.lower():
            os.startfile("C:/Program Files/Microsoft VS Code/Code.exe")
            time.sleep(1)

        elif "open steam" in query.lower():
            os.startfile("C:/Program Files (x86)/Steam/steam.exe")
            time.sleep(1)

#-------------------------Usual Commands--------------------------------------
        elif 'the time' in query.lower():
            nTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(nTime)
            speak("There is the time you want"+nTime)
            time.sleep(1)

        elif 'exit' in query.lower():
            requestPack.exitR()

#-------------------------Email--------------------------------------
        elif 'send email to echo' in query.lower():
            try:
                speak("Okay! What shoul I sent?")
                mail=emailCommand()
                mail
                to = "dev.echore08@gmail.com"
                sendEmail(to,mail)
                speak("Email sended")
            except Exception as e:
                print(e)
            time.sleep(1)
        
        elif 'send email to someone' in query.lower():
            try:
                speak("Okay! What shoul I sent?")
                mail=emailCommand()
                mail
                to =input("Enter a valid email address to send: ")
                sendEmail(to,mail)
                speak("Email sended")
            except Exception as e:
                print(e)
            time.sleep(1)

#
    except Exception as e:
        print("Enjoying the Silence? What a drag")
        speak("Enjoying the Silence? What a drag")