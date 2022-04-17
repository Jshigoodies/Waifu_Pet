import voice_audio as va
from colors import COLOR

# make it so you can ask for her to speak in a specific langauge

conditions = va.Reset(9)

while True:
    # va.respond(text="chichi there is a lot of wind It is very windy It's also snowing wind windy blowing snow santa morning", repeat_condition=conditions) # temporary
    text = va.get_audio()
    text = text.lower()
    print(COLOR.RESET + "you said:", text)  # comment out

    va.respond(text=text, repeat_condition=conditions)
