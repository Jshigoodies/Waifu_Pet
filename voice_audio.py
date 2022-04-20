import playsound
from playsound import playsound
import speech_recognition as sr
from colors import COLOR
import numpy
import random

# initialize a global array of strings. Such as greetings. Takes in all the "hello", "hi", "how are you", "howdy",

# all possible words to trigger a response

hello = ["hello", "greetings", "bonjour", "hi", "hey", "howdy"]  # all the ways to greet someone
chat_afraid_of_heat = ["hot", "burning", "blazing", "flaming", "fire", "scorching", "fiery"]

chat_training = ["count", "counting"]
when_it_rains = ["rain", "raining", "rainfall", "precipitation", "raindrops", "rainstorm", "hurricane", "thunder",
                 "storm", "rainwater", "rainy", "flood", "flooding", "hail", "pouring", "umbrella"]
when_the_sun_is_out = ["sun", "sunny", "bright", "outside", "outdoors", "outdoor"]
when_its_windy = ["wind"]
when_the_wind_is_blowing = ["blowing", "windy"]
when_it_snows = ["winter", "snow", "snowing", "snowflakes", "snowball", "snowman", "santa", "snowy"]
good_morning = ["morning", "a.m.", "early", "sunrise"]
good_afternoon = ["afternoon"]
good_evening = ["evening"]
good_night = ["sleep", "tired", "sleepy", "nap", "snooze", "slumber", "bed", "stress", "stressed"]
about_qiqi = [] # don't really need this
about_us_memory = ["memory", "memorizing", "remember", "remind", "forgot", "forget"]
# where i am ^^^
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
chat_talking_to_herself = ["do you know what"]  # i might need to figure out a phrase instead of using one word
# i can try string.find("do you know what")


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
    print(text_array)

    if "chichi" not in text_array:
        # print("i am here") # weird bug
        return

    if random.choice([1, 1, 1, 1, 1, 1, 0, 0]) == 1:
        for word in text_array:  # one for each word
            if check_array(word, repeat_condition=repeat_condition):
                understand = True
    else:
        print(COLOR.RED + "Did you ask me something? Sorry... I forgot.")
        playsound("audio\english\VO_Qiqi_About_Qiqi.mp3")
        return

    # make a for loop for specific phrases or if statments. Whichever works !!!! important

    if not understand:
        print(COLOR.RED + "What's going on?")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_01.mp3")

    repeat_condition.restart()  # back to false


def check_array(text, repeat_condition):
    # print(text)

    if text in hello and repeat_condition.stop[0] == False:
        repeat_condition.stop[0] = True
        print(COLOR.RED + "I am Qiqi. I am a zombie. And I forgot what comes next.")
        playsound("audio\english\VO_Qiqi_Hello.mp3")
    elif text in chat_afraid_of_heat and repeat_condition.stop[1] == False:
        repeat_condition.stop[1] = True
        print(COLOR.RED + "Let's go somewhere cooler.")
        playsound("audio\english\VO_Qiqi_Chat_-_Afraid_of_Heat.mp3")
    elif text in chat_training and repeat_condition.stop[2] == False:
        repeat_condition.stop[2] = True
        print(COLOR.RED + "One, two, three, four. Two, two, three, four...")
        playsound("audio\english\VO_Qiqi_Chat_-_Training.mp3")
    elif text in when_it_rains and repeat_condition.stop[3] == False:
        repeat_condition.stop[3] = True
        print(COLOR.RED + "I forgot my umbrella again.")
        playsound("audio\english\VO_Qiqi_When_It_Rains.mp3")
    elif text in when_the_sun_is_out and repeat_condition.stop[4] == False:
        repeat_condition.stop[4] = True
        print(COLOR.RED + "I should have stayed indoors today.")
        playsound("audio\english\VO_Qiqi_When_the_Sun_Is_Out.mp3")
    elif text in when_its_windy and repeat_condition.stop[5] == False:
        repeat_condition.stop[5] = True
        print(COLOR.RED + "The wind is... frigid. I like it.")
        playsound("audio\english\VO_Qiqi_When_It's_Windy.mp3")
    elif text in when_the_wind_is_blowing and repeat_condition.stop[6] == False:
        repeat_condition.stop[6] = True
        print(COLOR.RED + "Hold my hand please. This wind could blow me away.")
        playsound("audio\english\VO_Qiqi_When_the_Wind_Is_Blowing.mp3")
    elif text in when_it_snows and repeat_condition.stop[7] == False:
        repeat_condition.stop[7] = True
        print(COLOR.RED + "I want to build a snowman. Will you help?")
        playsound("audio\english\VO_Qiqi_When_It_Snows.mp3")
    elif text in good_morning and repeat_condition.stop[8] == False:
        repeat_condition.stop[8] = True
        print(COLOR.RED + "Morning means it's time to check my diary. Because my diary reminds me what I'm supposed to do in the morning.")
        playsound("audio\english\VO_Qiqi_Good_Morning.mp3")
    elif text in good_afternoon and repeat_condition.stop[9] == False:
        repeat_condition.stop[9] = True
        print(COLOR.RED + "I just remembered something. I forgot to help Dr. Baizhu prepare medications.")
        playsound("audio\english\VO_Qiqi_Good_Afternoon.mp3")
    elif text in good_evening and repeat_condition.stop[10] == False:
        repeat_condition.stop[10] = True
        print(COLOR.RED + "Good evening. How was your day? My day was fine, I think. But I can't remember.")
        playsound("audio\english\VO_Qiqi_Good_Evening.mp3")
    elif text in good_night and repeat_condition.stop[11] == False:
        repeat_condition.stop[11] = True
        print(COLOR.RED + "It's time for you to sleep now. I will do my stretches. ...Do not watch me please.")
        playsound("audio\english\VO_Qiqi_Good_Night.mp3")
    elif text in about_us_memory and repeat_condition.stop[12] == False:
        print(COLOR.RED + "I have a poor memory for most things. But as far as I know, that doesn't matter.")
        playsound("audio\english\VO_Qiqi_About_Us_-_Memory.mp3")
    else:
        return False
    return True
