import pyttsx3
from datetime import datetime

def run():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    text = f"Agora são {hour} horas  e {minute} minutos."

    print(f'speaking: {text}')
    en = pyttsx3.init()
    en.say(text)
    en.runAndWait()

if __name__ == "__main__":
    run()