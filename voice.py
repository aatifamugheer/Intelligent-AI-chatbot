import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio=r.listen(source)

    try:

        return r.recognize_google(audio)

    except:

        return ""