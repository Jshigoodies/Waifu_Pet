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
chat_talking_to_herself = []
chat_afraid_of_heat = []
chat_training = []
when_it_rains = ["rain", "raining", "rainfall", "precipitation", "raindrops", "rainstorm", "hurricane", "thunder", "storm", "rainwater", "rainy", "flood", "flooding", "hail", "pouring", "umbrella"]
when_the_sun_is_out = []
when_its_windy = []
when_the_wind_is_blowing = ["blowing", "windy"]  # when the wind is blowing
when_it_snows = ["winter", "snow", "snowing", "snowflakes", "snowball", "snowman", "santa"]
good_morning = ["morning", "a.m.", "early", "sunrise"]
good_afternoon = ["afternoon"]  # ADD THIS #ADD THIS
good_evening = ["evening"]  # ADD THIS #ADD THIS
good_night = []
about_qiqi = []
about_us_memory = []
about_us_memory_of_training = []
about_the_vision = []
something_to_share = []
interesting_things = []
about_baizhu = []


# sun is out, afraid of heat


# make a method that checks the input text. Return a string of the audio file back. Use playsound to play the sound.

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)  # find the microphone
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print(
                COLOR.RED + "*Qiqi could not hear you*")  # maybe get rid of it because I'm not really going to talk all the time

    return said


def respond(text):  # I need a new fking method
    pass


def check_array(text):
    pass