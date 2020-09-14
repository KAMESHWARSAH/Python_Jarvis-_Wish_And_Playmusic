import pyttsx3 
import speech_recognition as sr 
import os
import datetime
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Kameshwar  !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Kameshwar !")   

    else:
        speak("Good Evening Kameshwar!")  

    speak("I am your Jarvis . Please tell me how may I help you Kameshwar ")       

def takeCommand():
   

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
           
        print("Say that again please...")  
        return "None"
    return query

if _name_ == "_main_":
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'play music' in query:
            music_dir = 'D:\\song\\OLD SONG\\kumar sanu' 
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))
