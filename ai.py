import speech_recognition as sr
import os
from AppOpener import *
import time
import random
import pyttsx3
import wikipedia
def speak(write):
    speach=pyttsx3.init()
    speach.say(write)
    speach.runAndWait()
r = sr.Recognizer()
def search():
     result = wikipedia.search(text)
     print(result)
with sr.Microphone() as source:
    speak("hello how can i help you")
    print("Speak Anything :")
    audio = r.listen(source, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio, language="en-us")
        print(text)  
        if 'open vs code' in text.lower():
            speak("opening vs code")
        else:
            text = text.lower().replace('plus', '+').replace('minus', '-').replace('times', '*').replace('divided by', '/')
            text = text.replace('x', '*')  # Ensure this replacement is before eval
            try:
                result = eval(text)
                speak(str(result))
                print(result)
            except:
                try:
                    result = wikipedia.summary(text)
                    print(result)
                    speak(result)
                except:
                    speak('sorry, I could not find any information about that')
    except Exception as e:
        speak("Sorry, I could not recognize what you said")