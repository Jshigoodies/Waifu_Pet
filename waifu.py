import numpy
from discord import VoiceClient
from discord.ext import commands
from discord import FFmpegOpusAudio, File
import random
import time
# ------------------------

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


# -----------------------


class Reset:
    def __init__(self, num):
        self.size_num = num
        self.stop = numpy.zeros(1, dtype=bool)

    def create(self):
        self.stop = numpy.zeros(self.size_num, dtype=bool)

    def restart(self):
        self.stop = numpy.zeros(self.size_num, dtype=bool)


class Voice_audio:
    def __init__(self, channel, voice, source, text_channel, audio_num):
        self.channel = channel
        self.voice = voice
        self.source = source
        self.text_channel = text_channel
        self.audio_num = audio_num

condition = Reset(34)
va = Voice_audio(None, None, None, None, -1)
bot = commands.Bot(command_prefix="Qiqi ")
audio_texts = ["I am Qiqi. I am a zombie. And I forgot what comes next.",
               "Let's go somewhere cooler.",
               "One, two, three, four. Two, two, three, four...",
               "I forgot my umbrella again.",
               "I should have stayed indoors today.",
               "The wind is... frigid. I like it.",
               "Hold my hand please. This wind could blow me away.",
               "I want to build a snowman. Will you help?",
               "Morning means it's time to check my diary. Because my diary reminds me what I'm supposed to do in the morning.",
               "I just remembered something. I forgot to help Dr. Baizhu prepare medications.",
               "Good evening. How was your day? My day was fine, I think. But I can't remember.",
               "It's time for you to sleep now. I will do my stretches. ...Do not watch me please.",
               "I have a poor memory for most things. But as far as I know, that doesn't matter.",
               "I started memory training exercises recently. So don't you worry, I won't forget who you are.",
               "My Vision can't turn back time. But at least it gives me the power to protect the people that matter most.",
               "I may be a corpse, but I am in much better physical condition than Dr. Baizhu.",
               "Sometimes I see finches near the pharmacy. A nice little group of finches.",
               "I can never remember Dr. Baizhu's face. But I don't mind.",
               "Warm. Fake smile. Death. I despise Hu Tao.",
               "Sounds like a historical artifact to me.",
               "Remind me, have I met him before?",
               "Uh... who?",
               "Cute. Like a nice little finch.",
               "On some nights, I almost feel like someone is doing stretches together with me. But maybe I just have an overactive imagination.",
               "I perform stretches regularly to help me maintain the same range of movement as a normal human being. But as soon as I stop doing them, the rigor mortis starts to set in again.",
               "Some people want to take advantage of me. Others are terrified of me. But you... You are not like any of those people.",
               "Since we first met, I have had a warm feeling inside. Not the kind of warmth that makes me feel rotten and disgusting and closer to death. The other kind of warmth. The one that happens inside my heart. Thank you. I am happy. Sadly I only recognize the current you. If I forget you... No. I will order myself to remember you.",
               "In the past, my only thought was: I must stay alive. Even though I didn't know what to live for. But now, I think I know. I want to live with you. I want to ask, can we stay together, for the rest of life, until death? Yes or no? Yes? Is that your real answer? Good, excellent. I promise to always protect you.",
               "I want to have a pet. For example, a nice little finch.",
               "I don't know why, but high temperatures make me feel rotten and disgusting. And closer to death.",
               "I like coconut milk... But, I don't know what it tastes like.",
               "Many happy returns. Here is a bag of herbal medicine for you. You must be very surprised that I remembered? Let me explain. Last time you told me, I wrote your birthday down on a piece of paper. If I look at something once a day, it eventually goes into my long-term memory, and it will stay there forever.",
               "Ah, I understand. When I get stronger, I need to put more effort into controlling my strength.",
               "In the past, I did not understand the idea of becoming stronger than I already was. Now that I understand it well, I wish I was just a little stronger still."]

@bot.command()
async def bruh(ctx):
    await ctx.send("bruh")


@bot.command()
async def stop(ctx):
    exit(0)


@bot.command()
async def join(ctx):
    va.channel = ctx.message.author.voice.channel
    va.voice = await va.channel.connect()
    va.text_channel = ctx.message.channel
    condition.create()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("Qiqi "):
        channel = message.channel
        text = message.content
        voice = message.author.voice.channel
        args = message.content.split(" ")
        # -------
        # for i in args:
        #     print(i)
        # -------

        if len(args) == 2:
            await bot.process_commands(message)  # omg this is what i needed
        elif len(args) != 2:
            num = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4])
            understand = False
            if num == 1:
                for word in args:  # one for each word
                    if check_word(word, condition):
                        await va.text_channel.send(audio_texts[va.audio_num])
                        understand = True
                if not understand:
                    await va.text_channel.send("What's going on?")
                    va.source = FFmpegOpusAudio(
                        "audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_01.mp3")
                    va.voice.play(va.source)
                condition.restart()
                return
            elif num == 2:
                await va.text_channel.send("Did you ask me something? Sorry... I forgot.")
                va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Qiqi.mp3")
                va.voice.play(va.source)
                return
            elif num == 3:
                await va.text_channel.send("Hey, do you know what? Neither do I. I already forgot.")
                va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Chat_-_Talking_to_Herself.mp3")
                va.voice.play(va.source)
                return
            else:  # num == 4
                await va.text_channel.send("Sorry, I have no idea.")
                va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Least_Favorite_Food.mp3")
                va.voice.play(va.source)
                return

def check_word(text, repeat_condition):
    if text in hello and repeat_condition.stop[0] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 0
        repeat_condition.stop[0] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Hello.mp3")
        va.voice.play(va.source)
    elif text in chat_afraid_of_heat and repeat_condition.stop[1] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 1
        repeat_condition.stop[1] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Chat_-_Afraid_of_Heat.mp3")
        va.voice.play(va.source)
    elif text in chat_training and repeat_condition.stop[2] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 2
        repeat_condition.stop[2] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Chat_-_Training.mp3")
        va.voice.play(va.source)
    elif text in when_it_rains and repeat_condition.stop[3] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 3
        repeat_condition.stop[3] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_When_It_Rains.mp3")
        va.voice.play(va.source)
    elif text in when_the_sun_is_out and repeat_condition.stop[4] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 4
        repeat_condition.stop[4] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_When_the_Sun_Is_Out.mp3")
        va.voice.play(va.source)
    elif text in when_its_windy and repeat_condition.stop[5] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 5
        repeat_condition.stop[5] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_When_It's_Windy.mp3")
        va.voice.play(va.source)
    elif text in when_the_wind_is_blowing and repeat_condition.stop[6] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 6
        repeat_condition.stop[6] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_When_the_Wind_Is_Blowing.mp3")
        va.voice.play(va.source)
    elif text in when_it_snows and repeat_condition.stop[7] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 7
        repeat_condition.stop[7] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_When_It_Snows.mp3")
        va.voice.play(va.source)
    elif text in good_morning and repeat_condition.stop[8] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 8
        repeat_condition.stop[8] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Good_Morning.mp3")
        va.voice.play(va.source)
    elif text in good_afternoon and repeat_condition.stop[9] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 9
        repeat_condition.stop[9] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Good_Afternoon.mp3")
        va.voice.play(va.source)
    elif text in good_evening and repeat_condition.stop[10] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 10
        repeat_condition.stop[10] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Good_Evening.mp3")
        va.voice.play(va.source)
    elif text in good_night and repeat_condition.stop[11] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 11
        repeat_condition.stop[11] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Good_Night.mp3")
        va.voice.play(va.source)
    elif text in about_us_memory and repeat_condition.stop[12] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 12
        repeat_condition.stop[12] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Us_-_Memory.mp3")
        va.voice.play(va.source)
    elif text in about_us_memory_of_training and repeat_condition.stop[13] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 13
        repeat_condition.stop[13] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Us_-_Memory_Training.mp3")
        va.voice.play(va.source)
    elif text in about_the_vision and repeat_condition.stop[14] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 14
        repeat_condition.stop[14] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_the_Vision.mp3")
        va.voice.play(va.source)
    elif text in something_to_share and repeat_condition.stop[15] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 15
        repeat_condition.stop[15] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Something_to_Share.mp3")
        va.voice.play(va.source)
    elif text in interesting_things and repeat_condition.stop[16] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 16
        repeat_condition.stop[16] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Interesting_Things.mp3")
        va.voice.play(va.source)
    elif text in about_baizhu and repeat_condition.stop[17] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 17
        repeat_condition.stop[17] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Baizhu.mp3")
        va.voice.play(va.source)
    elif text in about_hutao and repeat_condition.stop[18] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 18
        repeat_condition.stop[18] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Hu_Tao.mp3")
        va.voice.play(va.source)
    elif text in about_xiao_name and repeat_condition.stop[19] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 19
        repeat_condition.stop[19] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Xiao_-_Name.mp3")
        va.voice.play(va.source)
    elif text in about_xiao_memory and repeat_condition.stop[20] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 20
        repeat_condition.stop[20] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Xiao_-_Memory.mp3")
        va.voice.play(va.source)
    elif text in about_xinyan and repeat_condition.stop[21] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 21
        repeat_condition.stop[21] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Xinyan.mp3")
        va.voice.play(va.source)
    elif text in about_yaoyao and repeat_condition.stop[22] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 22
        repeat_condition.stop[22] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Yaoyao.mp3")
        va.voice.play(va.source)
    elif text in about_dusky_ming and repeat_condition.stop[23] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 23
        repeat_condition.stop[23] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_About_Dusky_Ming.mp3")
        va.voice.play(va.source)
    elif text in more_about_qiqi_two and repeat_condition.stop[24] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 24
        repeat_condition.stop[24] = True
        va.source = FFmpegOpusAudio("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_02.mp3")
        va.voice.play(va.source)
    elif text in more_about_qiqi_three and repeat_condition.stop[25] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 25
        repeat_condition.stop[25] = True
        va.source = FFmpegOpusAudio("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_03.mp3")
        va.voice.play(va.source)
    elif text in more_about_qiqi_four and repeat_condition.stop[26] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 26
        repeat_condition.stop[26] = True
        va.source = FFmpegOpusAudio("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_04.mp3")
        va.voice.play(va.source)
    elif text in more_about_qiqi_five and repeat_condition.stop[27] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 27
        repeat_condition.stop[27] = True
        va.source = FFmpegOpusAudio("audio\english\more_about_qiqi_friendship\VO_Qiqi_More_About_Qiqi_-_05.mp3")
        va.voice.play(va.source)
    elif text in qiqi_hobbies and repeat_condition.stop[28] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 28
        repeat_condition.stop[28] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Hobbies.mp3")
        va.voice.play(va.source)
    elif text in qiqi_troubles and repeat_condition.stop[29] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 29
        repeat_condition.stop[29] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Troubles.mp3")
        va.voice.play(va.source)
    elif text in favorite_food and repeat_condition.stop[30] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 30
        repeat_condition.stop[30] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Favorite_Food.mp3")
        va.voice.play(va.source)
    elif text in birthday and repeat_condition.stop[31] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 31
        repeat_condition.stop[31] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Birthday.mp3")
        va.voice.play(va.source)
    elif text in feelings_about_ascension_building_up and repeat_condition.stop[32] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 32
        repeat_condition.stop[32] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Feelings_About_Ascension_-_02.mp3")
        va.voice.play(va.source)
    elif text in feelings_about_ascension_climax and repeat_condition.stop[33] == False:
        while va.voice.is_playing() == True:
            time.sleep(2)
        va.audio_num = 33
        repeat_condition.stop[33] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Feelings_About_Ascension_-_03.mp3")
        va.voice.play(va.source)
    else:
        return False

    return True


bot.run("OTc0NzE3ODM3ODU3OTIzMDgy.G_4rfP.ZptvvhUStbJ005RXhBk1Zead2btR6hVa2EgbBA")
