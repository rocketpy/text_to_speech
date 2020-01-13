#  pip install gtts

import os
from gtts import gTTS


text = "Hello world"

print("Wait for result ..")
TTS = gTTS(text=text, lang='en-uk')

#  save to mp3 in current directory
TTS.save("new_voice.mp3")

#  play mp3 using the default app on your system
os.system("start new_voice.mp3")
