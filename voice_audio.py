import os
import time
import playsound
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from colors import COLOR

# initialize a global array of strings. Such as greetings. Takes in all the "hello", "hi", "how are you", "howdy",

# all possible words to trigger a response

hello = ["hello", "greetings", "bonjour", "hi", "hey", "howdy"]  # all the ways to greet someone
morning = ["morning", "a.m.", "early", "sunrise"]
rain = ["rain", "raining", "rainfall", "precipitation", "raindrops", "rainstorm", "hurricane", "thunder", "storm", "rainwater", "rainy", "flood", "flooding", "hail", "pouring", "umbrella"]
snow = ["winter", "snow", "snowing", "snowflakes", "snowball", "snowman", "santa"]
# make a method that checks the input text. Return a string of the audio file back. Use playsound to play the sound.

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)  # find the microphone
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print(COLOR.RED + "*Qiqi could not hear you*")  # maybe get rid of it because I'm not really going to talk all the time

    return said


# check the text that would play the right audio back
def check(text):
    # have a way to shut her up, maybe make a method for both shut up and un-shut up
    talk = False # if she said something, then i don't have to make her say nani-ka

    if "chichi" in text:  # you have to say her name
        text_array = text.split()

        for word in text_array:  # check each word probably slow as fk
            # print(word) # prints out what i said in a list

            if word in hello:  # change this later so get an array of greetings
                talk = True
                print(COLOR.RED + "Qiqi, I'm a jiangshi. Hm...? What else...")
                playsound("audio/hello.mp3")
            if word in morning:
                talk = True
                print(COLOR.RED + "It's morning already? What should I... I'll check my notes.")
                playsound("audio/good_morning.mp3")
            if word in rain:
                talk = True
                print(COLOR.RED + "Forgot an umbrella again.")
                playsound("audio/rain.mp3")
            if word in snow:
                talk = True
                print(COLOR.RED + "Wanna build a snowman... Can you help?")
                playsound("audio/snow.mp3")

        if not talk:  # did not say anything
            print(COLOR.RED + "What?")
            playsound("audio/nani_ka.mp3")

# a problem i found. If you say the same word 3 times. she will tell the same thing 3 times. Probably need a counter so she doesn't repeat the same sentence over and over again