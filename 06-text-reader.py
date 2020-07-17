import os
from gtts import gTTS
from pygame import mixer

print('carregando o arquivo, aguarde')

filename = input('informa o caminho do arquivo: ')

if os.path.isfile(filename):
    file = open(filename)
    filedata = file.read()
    voice_path = '_files/voice.mp3'

    voice = gTTS(filedata, lang='pt')
    voice.save(voice_path)

    mixer.init()
    mixer.music.load(voice_path)
    mixer.music.play()

    x = input('Pressione qualquer tecla para finalizar')