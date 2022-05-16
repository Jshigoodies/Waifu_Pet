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
about_qiqi = []  # don't really need this
about_us_memory = ["memory", "memorizing", "remember", "remind", "forgot", "forget", "remembered", "memorized",
                   "memorize"]
about_us_memory_of_training = ["memory", "memorizing", "remember", "remind", "forgot", "forget", "remembered",
                               "memorized", "memorize"]
about_the_vision = ["vision", "eyes", "eyeball", "sight", "eyesight", "view"]
something_to_share = ["physical", "dead", "corpse", "health"]
interesting_things = ["finches", "pharmacy"]
about_baizhu = ["baizhu", "baijiu"]
about_hutao = ["hutao", "hotel"]
about_xiao_name = ["xiao", "shell"]
about_xiao_memory = ["xiao", "shell"]
about_xinyan = ["xinyan", "who", "yourself"]
about_yaoyao = ["cute", "nice", "wholesome", "adorable", "sweet", "lovable"]
about_dusky_ming = ["stretch", "stretches", "stretching", "paranoid"]
_about_qiqi_one = []  # do not need this
more_about_qiqi_two = ["stretch", "stretches", "stretching"]  # file num 2
more_about_qiqi_three = ["people", "terrified"]  # file num 3
more_about_qiqi_four = ["feelings", "love"]  # file num 4
more_about_qiqi_five = ["past", "love"]  # file num 5
qiqi_hobbies = ["hobby", "hobbies", "pet", "dog", "cat", "finch"]
qiqi_troubles = ["temperature", "heat", "hot", "death"]
favorite_food = ["food", "milk", "coconut"]
birthday = ["birthday"]
feelings_about_ascension_building_up = ["effort", "strength", "strong", "work"]
feelings_about_ascension_climax = ["strength", "strong"]
# where i am ^^^^^^^^^^^^
# phrases that are need to activate this
chat_talking_to_herself = ["do you know what"]  # i might need to figure out a phrase instead of using one word
least_favorite_food = []


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
        if "qiqi" not in text_array:
            return
    num = random.choice([1, 1, 1, 1, 1, 1, 1, 2, 3, 4])
    if num == 1:
        for word in text_array:  # one for each word
            if check_array(word, repeat_condition=repeat_condition):
                understand = True
    elif num == 2:
        print(COLOR.RED + "Did you ask me something? Sorry... I forgot.")
        playsound("audio\english\VO_Qiqi_About_Qiqi.mp3")
        return
    elif num == 3:
        print(COLOR.RED + "Hey, do you know what? Neither do I. I already forgot.")
        playsound("audio\english\VO_Qiqi_Chat_-_Talking_to_Herself.mp3")
        return
    else:  # num == 4
        print(COLOR.RED + "Sorry, I have no idea.")
        playsound("audio\english\VO_Qiqi_Least_Favorite_Food.mp3")
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
        print(
            COLOR.RED + "Morning means it's time to check my diary. Because my diary reminds me what I'm supposed to do in the morning.")
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
        repeat_condition.stop[12] = True
        print(COLOR.RED + "I have a poor memory for most things. But as far as I know, that doesn't matter.")
        playsound("audio\english\VO_Qiqi_About_Us_-_Memory.mp3")
    elif text in about_us_memory_of_training and repeat_condition.stop[13] == False:
        repeat_condition.stop[13] = True
        print(
            COLOR.RED + "I started memory training exercises recently. So don't you worry, I won't forget who you are.")
        playsound("audio\english\VO_Qiqi_About_Us_-_Memory_Training.mp3")
    elif text in about_the_vision and repeat_condition.stop[14] == False:
        repeat_condition.stop[14] = True
        print(
            COLOR.RED + "My Vision can't turn back time. But at least it gives me the power to protect the people that matter most.")
        playsound("audio\english\VO_Qiqi_About_the_Vision.mp3")
    elif text in something_to_share and repeat_condition.stop[15] == False:
        repeat_condition.stop[15] = True
        print(COLOR.RED + "I may be a corpse, but I am in much better physical condition than Dr. Baizhu.")
        playsound("audio\english\VO_Qiqi_Something_to_Share.mp3")
    elif text in interesting_things and repeat_condition.stop[16] == False:
        repeat_condition.stop[16] = True
        print(COLOR.RED + "Sometimes I see finches near the pharmacy. A nice little group of finches.")
        playsound("audio\english\VO_Qiqi_Interesting_Things.mp3")
    elif text in about_baizhu and repeat_condition.stop[17] == False:
        repeat_condition.stop[17] = True
        print(COLOR.RED + "I can never remember Dr. Baizhu's face. But I don't mind.")
        playsound("audio\english\VO_Qiqi_About_Baizhu.mp3")
    elif text in about_hutao and repeat_condition.stop[18] == False:
        repeat_condition.stop[18] = True
        print(COLOR.RED + "Warm. Fake smile. Death. I despise Hu Tao.")
        playsound("audio\english\VO_Qiqi_About_Hu_Tao.mp3")
    elif text in about_xiao_name and repeat_condition.stop[19] == False:
        repeat_condition.stop[19] = True
        print(COLOR.RED + "Sounds like a historical artifact to me.")
        playsound("audio\english\VO_Qiqi_About_Xiao_-_Name.mp3")
    elif text in about_xiao_memory and repeat_condition.stop[20] == False:
        repeat_condition.stop[20] = True
        print(COLOR.RED + "Remind me, have I met him before?")
        playsound("audio\english\VO_Qiqi_About_Xiao_-_Memory.mp3")
    elif text in about_xinyan and repeat_condition.stop[21] == False:
        repeat_condition.stop[21] = True
        print(COLOR.RED + "Uh... who?")
        playsound("audio\english\VO_Qiqi_About_Xinyan.mp3")
    elif text in about_yaoyao and repeat_condition.stop[22] == False:
        repeat_condition.stop[22] = True
        print(COLOR.RED + "Cute. Like a nice little finch.")
        playsound("audio\english\VO_Qiqi_About_Yaoyao.mp3")
    elif text in about_dusky_ming and repeat_condition.stop[23] == False:
        repeat_condition.stop[23] = True
        print(
            COLOR.RED + "On some nights, I almost feel like someone is doing stretches together with me. But maybe I just have an overactive imagination.")
        playsound("audio\english\VO_Qiqi_About_Dusky_Ming.mp3")
    elif text in more_about_qiqi_two and repeat_condition.stop[24] == False:
        repeat_condition.stop[24] = True
        print(
            COLOR.RED + "I perform stretches regularly to help me maintain the same range of movement as a normal human being. But as soon as I stop doing them, the rigor mortis starts to set in again.")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_02.mp3")
    elif text in more_about_qiqi_three and repeat_condition.stop[25] == False:
        repeat_condition.stop[25] = True
        print(
            COLOR.RED + "Some people want to take advantage of me. Others are terrified of me. But you... You are not like any of those people.")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_03.mp3")
    elif text in more_about_qiqi_four and repeat_condition.stop[26] == False:
        repeat_condition.stop[26] = True
        print(
            COLOR.RED + "Since we first met, I have had a warm feeling inside. Not the kind of warmth that makes me feel rotten and disgusting and closer to death. The other kind of warmth. The one that happens inside my heart. Thank you. I am happy. Sadly I only recognize the current you. If I forget you... No. I will order myself to remember you.")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_04.mp3")
    elif text in more_about_qiqi_five and repeat_condition.stop[27] == False:
        repeat_condition.stop[27] = True
        print(
            COLOR.RED + "In the past, my only thought was: I must stay alive. Even though I didn't know what to live for. But now, I think I know. I want to live with you. I want to ask, can we stay together, for the rest of life, until death? Yes or no? Yes? Is that your real answer? Good, excellent. I promise to always protect you.")
        playsound("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_05.mp3")
    elif text in qiqi_hobbies and repeat_condition.stop[28] == False:
        repeat_condition.stop[28] = True
        print(COLOR.RED + "I want to have a pet. For example, a nice little finch.")
        playsound("audio\english\VO_Qiqi_Hobbies.mp3")
    elif text in qiqi_troubles and repeat_condition.stop[29] == False:
        repeat_condition.stop[29] = True
        print(
            COLOR.RED + "I don't know why, but high temperatures make me feel rotten and disgusting. And closer to death.")
        playsound("audio\english\VO_Qiqi_Troubles.mp3")
    elif text in favorite_food and repeat_condition.stop[30] == False:
        repeat_condition.stop[30] = True
        print(COLOR.RED + "I like coconut milk... But, I don't know what it tastes like.")
        playsound("audio\english\VO_Qiqi_Favorite_Food.mp3")
    elif text in birthday and repeat_condition.stop[31] == False:
        repeat_condition.stop[31] = True
        print(
            COLOR.RED + "Many happy returns. Here is a bag of herbal medicine for you. You must be very surprised that I remembered? Let me explain. Last time you told me, I wrote your birthday down on a piece of paper. If I look at something once a day, it eventually goes into my long-term memory, and it will stay there forever.")
        playsound("audio\english\VO_Qiqi_Birthday.mp3")
    elif text in feelings_about_ascension_building_up and repeat_condition.stop[32] == False:
        repeat_condition.stop[32] = True
        print(
            COLOR.RED + "Ah, I understand. When I get stronger, I need to put more effort into controlling my strength.")
        playsound("audio\english\VO_Qiqi_Feelings_About_Ascension_-_02.mp3")
    elif text in feelings_about_ascension_climax and repeat_condition.stop[33] == False:
        repeat_condition.stop[33] = True
        print(
            COLOR.RED + "In the past, I did not understand the idea of becoming stronger than I already was. Now that I understand it well, I wish I was just a little stronger still.")
        playsound("audio\english\VO_Qiqi_Feelings_About_Ascension_-_03.mp3")
    else:
        return False
    return True
