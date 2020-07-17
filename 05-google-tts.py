from gtts import gTTS
from pygame import mixer

voice = gTTS('Boa noite Marina. Como você está meu anjo?', lang='pt')
voice.save('_files/voice.mp3')

mixer.init()
mixer.music.load('_files/voice.mp3')
mixer.music.play()

x = input('Pressione qualquer tecla para finalizar')