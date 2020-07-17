import pyttsx3
from datetime import datetime

username = 'Felipe'

now = datetime.now()

hour = now.hour
minute = now.minute

en = pyttsx3.init()

en.say(f"Bem vindo {username}. Agora são {hour} horas  e {minute} minutos")

en.runAndWait()