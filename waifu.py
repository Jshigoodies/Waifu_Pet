import numpy
from discord.ext import commands
from discord import FFmpegOpusAudio, File
import random

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
    def __init__(self, channel, voice, source, text_channel):
        self.channel = channel
        self.voice = voice
        self.source = source
        self.text_channel = text_channel


condition = Reset(34)
va = Voice_audio(None, None, None, None)
audio_num = -1
bot = commands.Bot(command_prefix="Qiqi ")
audio_texts = ["I am Qiqi. I am a zombie. And I forgot what comes next.", "Let's go somewhere cooler.", "One, two, three, four. Two, two, three, four..."]

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
        for i in args:
            print(i)
        # -------

        if len(args) == 2:
            await bot.process_commands(message)  # omg this is what i needed
        elif len(args) != 2:
            understand = False
            num = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4])
            if num == 1:
                for word in args:  # one for each word
                    if check_word(word, condition):
                        await va.text_channel.send(audio_texts[audio_num])
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
        audio_num = 0
        repeat_condition.stop[0] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Hello.mp3")
        va.voice.play(va.source)
    elif text in chat_afraid_of_heat and repeat_condition.stop[1] == False:
        audio_num = 1
        repeat_condition.stop[1] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Chat_-_Afraid_of_Heat.mp3")
        va.voice.play(va.source)
    elif text in chat_training and repeat_condition.stop[2] == False:
        audio_num = 2
        repeat_condition.stop[2] = True
        va.source = FFmpegOpusAudio("audio\english\VO_Qiqi_Chat_-_Training.mp3")
        va.voice.play(va.source)
    else:
        return False

    return True


bot.run("OTc0NzE3ODM3ODU3OTIzMDgy.G_4rfP.ZptvvhUStbJ005RXhBk1Zead2btR6hVa2EgbBA")
