
import voice_audio as va
from colors import COLOR

while True:
    text = va.get_audio()
    text = text.lower()
    print(COLOR.RESET + "you said: ", text) # comment out

    va.check(text=text)

