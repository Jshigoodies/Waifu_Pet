import os
import time
import playsound
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from colors import COLOR
# make a method that checks the input text. Return a string of the audio file back. Use playsound to play the sound.

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)  # find the microphone
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))

    return said


# check the text that would play the right audio back
def check(text):
    if "morning" in text:
        print(COLOR.RED + COLOR.BOLD + "It's morning already? What should I... I'll check my notes.")
        playsound("audio/good_morning.mp3")
