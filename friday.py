import pyttsx3 as pts
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
import pyjokes
import requests
from bs4 import BeautifulSoup
import urllib.request
import re


core = pts.init('sapi5')
voices = core.getProperty('voices')
print(voices[1].id)
core.setProperty('voice',voices[1].id)
#voice test

curtime = datetime.datetime.now().strftime("%H %M")

s_rate = core.getProperty('rate')
core.setProperty('rate' , 180)


def speak(audio):
    core.say(audio)
    core.runAndWait()

def greet():
    speak("hello user , i'm your personal voice assistant")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning user ,")
        speak("the current time is" + curtime )

    elif hour >= 12 and hour < 18:
        speak("good afternoon user")
        speak("the current time is" + curtime)
    
    else :
        speak("good evening user")
        speak("the current time is " + curtime)

def voicecommand():
    

    m = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        m.pause_threshold = 1
        audio = m.listen(source)
    try:
        print("Understanding...")    
        inp = m.recognize_google(audio, language='en-in') 
        print(f"User said: {inp}\n")  
    except Exception :
           
        print("Say that again please...")   
        return "None" 
    return inp
 


if __name__ == '__main__':
    greet()
    speak("how may i help you ?")
    while True:
        inp =  voicecommand().lower()
        if 'wikipedia' in inp:
            speak("Getting that from wikipedia")
            inp = inp.replace("wikipedia" , "")
            out = wikipedia.summary(inp , sentences = 2)
            speak("According to wikipedia")
            print(out)
            speak(out)
        elif 'shutdown' in inp:
            speak("preparing to shutdown your computer")
            os.system("shutdown /s /t 5")
        elif 'restart' in inp:
            speak("preparing to restart your pc")
            os.system("shutdown /r /t 5")
        elif 'lock' in inp:
            speak("preparing to lock your pc")
            os.system("shutdown -l")
        elif 'open google' in inp:
            speak("alright opening google")
            webbrowser.open("https://www.google.com/")
        elif 'open youtube' in inp:
            speak("ok opening youtube")
            webbrowser.open("https://youtube.com/")
        elif 'rick roll'  in inp:            #easter egg 1
            speak("coming right up chief")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif 'coin' in inp:
            speak("flipping a coin")
            coin = random.randint(1,2)
            if coin == 1:
                speak("we've got ourselves a head")
            else:
                speak("we've got ourselves a tail")
        elif 'joke' in inp:
            speak(pyjokes.get_joke())
        elif 'join politics' in inp:        #easter egg 2
            speak("sure why not")
            webbrowser.open("https://www.youtube.com/watch?v=lSOAR9QBGtA")


        elif 'play music' in inp:
            speak("coming right up boss")
            hmusic = 'E:\\songs\\'
            song = os.listdir(hmusic)
            play = random.choice(song)
            os.startfile(play)

        elif 'introduce'  in inp or 'who are you' in inp or 'what are you' in inp:
            speak("my name is Friday and i'm your personal voice assistant , i can play music for you , flip coins , tell you a joke perhaps to lighten up your mood , get you wiki and google results ,want to know what's the weather like ,i can tell you that too, also there are several easter eggs that you can discover , have a good day")

        elif 'bye' in inp:
            speak('alright sir , have a great day')
            exit()
        
        elif 'are you single' in inp:         #easter egg 3
            speak('i am in relationship with your wifi')
        
        elif 'google' in inp:
            sc = inp.lower().split().index('google') 
            result = inp.split()[sc + 1:] 
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(result))

       

        elif 'temperature' in inp:
           search_key = inp
           retrieve = f"https://www.google.com/search?q={search_key}"  
           req = requests.get(retrieve)
           parse = BeautifulSoup(req.text,"html.parser")
           temperature = parse.find("div", class_="BNeawe").text
           speak(f"the current temperature is {temperature}")


        elif 'i am sad' in inp:
            speak('eating dark chocolate , helps elevate mood , while you do that ,here is  a song just for you')
            webbrowser.open("https://youtu.be/y6Sxv-sUYtM") 
        

        elif 'youtube' in inp:
            speak("What do you want to watch on youtube?")
            to_watch = voicecommand().replace(" ", "")
            
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+to_watch)
           
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
           
            webbrowser.open("https://www.youtube.com/watch?v="+video_ids[0])
            speak("there you go!")
