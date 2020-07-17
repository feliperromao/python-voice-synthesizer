from gtts import gTTS

def run(text):
    voice = gTTS(text, lang='pt')
    voice.save('../_files/voice.mp3')