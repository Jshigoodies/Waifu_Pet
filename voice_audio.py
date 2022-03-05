import os
import time
import playsound
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from colors import COLOR


# initialize a global arary of strings. Such as greetings. Takes in all the "hello", "hi", "how are you", "howdy",
# "greetings", "bonjour".


# make a method that checks the input text. Return a string of the audio file back. Use playsound to play the sound.

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)  # find the microphone
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print(COLOR.RED + "*Qiqi could not hear you*")

    return said


# check the text that would play the right audio back
def check(text):

    # have a way to shut her up, maybe make a method for both shut up and un-shut up

    if "chichi" in text: # you have to say her name
        if "hello" in text:  # change this later so get an array of greetings
            print(COLOR.RED + "Qiqi, I'm a jiangshi. Hm...? What else...")
            playsound("audio/hello.mp3")
        if "morning" in text:
            print(COLOR.RED + "It's morning already? What should I... I'll check my notes.")
            playsound("audio/good_morning.mp3")