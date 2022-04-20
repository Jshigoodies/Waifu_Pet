import voice_audio as va
from colors import COLOR

# make it so you can ask for her to speak in a specific langauge

conditions = va.Reset(13)

while True:
    # va.respond(text="chichi good afternoon", repeat_condition=conditions) # temporary
    text = va.get_audio()
    text = text.lower()
    print(COLOR.RESET + "you said:", text)  # comment out

    va.respond(text=text, repeat_condition=conditions)
