import datetime
import webbrowser
import pyttsx3
import self as self
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import random
import sys
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir..!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir..!")
    else:
        speak("Good Evening Sir...!")
    speak("i am Jarvis Your Assistant, Please Tell Me How may i Help You")

def take_command():        #it takes the input from the user as audio and returns the string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir Said: {query}\n")
    except Exception as e:
        #print(e)
        print('Say that Again Please...')
        return"None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rishabh1799@gmail.com','rishabh1799@75')
    server.sendmail('rishabh1799@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wish_me()
    while True:
        query1 = take_command().lower()
        if 'ok jarvis' in query1:
            speak("Searching For The Query")
            query1 = query1.replace('wikipedia','')
            results = wikipedia.summary(query1,sentences=2)
            speak("According To Google")
            webbrowser.open(results)
            print(results)
            speak(results)

        elif 'open youtube' in query1:
            webbrowser.open('youtube.com')

        elif 'open fb' in query1:
            webbrowser.open('facebook.com')

        elif 'open google' in query1:
            webbrowser.open('google.com')

        elif 'play music' in query1:
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,900)]))
        elif 'open gmail' in query1:
            webbrowser.open('gmail.com')

        elif 'fuck' in query1:
            speak("Sir,Please don't use the abusive word")

        elif 'excellent' in query1:
            speak('Thank You ,I am really thankful')

        elif 'time' in query1:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir,The Time is{strTime}")

        elif 'send a mail for me' in query1:
            try:
                speak("What should I say ?")
                content = take_command()
                to = 'rishabh1799@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                #print(e)
                speak("Sorry Sir,I am not able to send the Email at this moment")
