from gtts import gTTs

language="en"
text="Hi bro"

speech=gTTs(text=text,lang=language,slow=False)
speech.save("speech.mp3")