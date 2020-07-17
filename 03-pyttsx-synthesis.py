import pyttsx3

# Caso nao tenha o espeak pode ser utilziado o sapi5
# en = pyttsx3.init(sapi5)

en = pyttsx3.init()

en.setProperty('rate', 140)
en.setProperty('volume', 0.5)
en.setProperty('voice', b'brazil')
en.say("Bem vindo chefe!")
en.runAndWait()