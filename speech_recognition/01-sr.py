import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        recon.adjust_for_ambient_noise(source, duration=5)
        print('Diga algo ai chapa')
        audio = recon.listen(source)
        print(recon.recognize_sphinx(audio))


input('Pressione qualquer tecla para encerrar')