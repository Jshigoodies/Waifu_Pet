import os
import time
import playsound
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from colors import COLOR
import numpy

# initialize a global array of strings. Such as greetings. Takes in all the "hello", "hi", "how are you", "howdy",

# all possible words to trigger a response

hello = ["hello", "greetings", "bonjour", "hi", "hey", "howdy"]  # all the ways to greet someone
chat_afraid_of_heat = ["hot", "burning", "blazing", "flaming", "fire", "scorching", "fiery"]

chat_training = ["count", "counting"]
# stopped here ^^^^^
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

# phrases that are need to activate this
chat_talking_to_herself = []  # i might need to figure out a phrase instead of using one word


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


# global class
class Reset:
    def __init__(self, num):
        self.size_num = num
        self.stop = numpy.zeros(1, dtype=bool)

    def create(self):
        self.stop = numpy.zeros(self.size_num, dtype=bool)

    def restart(self):
        self.stop = numpy.zeros(self.size_num, dtype=bool)


# repeat_condition = Reset(3)


def respond(text, repeat_condition):  # I need a new fking method
    repeat_condition.create()
    # print(repeat_condition.size_num)
    # print(repeat_condition.stop[0])
    understand = False

    text_array = text.split()

    if "chichi" not in text_array:
        return

    for word in text_array:  # one for each word
        if check_array(word, repeat_condition=repeat_condition):
            understand = True

    # make a for loop for specific phrases!!!! important

    if not understand:
        print(COLOR.RED + "What's going on?")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_01.mp3")

    repeat_condition.restart()  # back to false


def check_array(text, repeat_condition):
    if text in hello and repeat_condition.stop[0] == False:
        print(COLOR.RED + "I am Qiqi. I am a zombie. And I forgot what comes next.")
        playsound("audio\english\VO_Qiqi_Hello.mp3")
        repeat_condition.stop[0] = True
        return True
    if text in chat_afraid_of_heat and repeat_condition.stop[1] == False:
        print(COLOR.RED + "Let's go somewhere cooler.")
        playsound("audio\english\VO_Qiqi_Chat_-_Afraid_of_Heat.mp3")
        repeat_condition.stop[1] = True


def check_good_day_array(text):
    pass
