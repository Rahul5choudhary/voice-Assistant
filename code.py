import pyttsx3
import datetime
import speech_recognition as sr
import os
import subprocess
import pyjokes 
import webbrowser
engine=pyttsx3.init()


if __name__ == '__main__': 
    clear = lambda: os.system('cls')


clear()
def speak(str):
  engine.say(str)
  engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(chunk_size=8192, sample_rate=44100, device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        print('Listening..')
        audio = r.listen(source)
        try:
            print('Recognizing..')
            #query = r.recognize_sphinx(audio)
            query = r.recognize_google(audio)
            return query
        except Exception:
            print('Oops! Did not catch that')
            return "None"
  
#speak('Rahul')
h=int(datetime.datetime.now().hour)
#print(h)
if h>=0 and h<=12:
 speak("Good morning Sir")
elif h>=12 and h<=18:
 speak("Good afternoon Sir")
else:
     speak("Good evening Sir")
     
speak("I am yor assistant robo 2 point O")

speak("What should i call you sir")
username=takecommand()
#username="Rahul"
speak("Welcome ")
speak(username)

speak("How can i help you")
speak(username)

while True:
    query=takecommand().lower()
    
    if 'how are you' in query:
        speak('I am fine, Thank you')
        speak("how are you")
        speak(username)
    elif "fine " in query:
        speak("It's good to know that you are fine")
    elif "exit" in query:
        speak("Thanks for giving me your time")
        exit()
    elif "shutdown" in query:
        subprocess.call(["shutdown","/r"])
    elif "who made you" in query:
        speak("I have been created by Rahul")
    elif "restart" in query:
       subprocess.call(["shutdown","/r"])
    elif "hibernate" in query:
        speak("Hibernating")
        subprocess.call("shutdown /h")
    elif "time" in query:
         v=(datetime.datetime.now().hour)
         speak("The time is")
         speak(v)
         speak("hours and")
         v=(datetime.datetime.now().minute)
         speak(v)
         speak("minutes")
    elif "joke" in query:
        speak(pyjokes.get_joke())
    elif "youtube" in query:
        speak("Opening Yotube")
        webbrowser.open("www.youtube.com")
    elif "google" in query:
         speak("Opening Google")
         webbrowser.open("www.google.com")
    elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")  
            print(query)         
            webbrowser.open(query) 
        
        