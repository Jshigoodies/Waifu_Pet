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
chat_talking_to_herself = []  # i might need to figure out a phrase instead of using one word
chat_afraid_of_heat = []
chat_training = []
when_it_rains = ["rain", "raining", "rainfall", "precipitation", "raindrops", "rainstorm", "hurricane", "thunder",
                 "storm", "rainwater", "rainy", "flood", "flooding", "hail", "pouring", "umbrella"]
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
about_hutao = []
about_xiao_name = []
about_xiao_memory = []
about_xinyan = []
about_yaoyao = []
about_dusky_ming = []
more_about_qiqi_one = []  # file num 1
more_about_qiqi_two = []  # file num 2
more_about_qiqi_three = []  # file num 3
more_about_qiqi_four = []  # file num 4
more_about_qiqi_five = []  # file num 5
qiqi_hobbies = []
qiqi_troubles = []
favorite_food = []
least_favorite_food = []
birthday = []
feelings_about_ascension_building_up = []
feelings_about_ascension_climax = []


# Only ascension phase 2 and 4 makes sense. The ogg files is labeled 2 and 3.

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
    understand = False
    stop = [False, False]  # don't repeat
    text_array = text.split()

    if "chichi" not in text_array:
        return

    for word in text_array:
        if check_array(word) and stop[0] == False:
            understand = True
            stop[0] = True

    if not understand:
        print(COLOR.RED + "What's going on?")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_01.mp3")


def check_array(text):
    if text in hello:
        print(COLOR.RED + "I am Qiqi. I am a zombie. And I forgot what comes next.")
        playsound("audio\english\VO_Qiqi_Hello.mp3")
        return True


def check_good_day_array(text):
    pass
