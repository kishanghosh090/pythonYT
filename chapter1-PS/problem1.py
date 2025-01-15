# problem1----------------------

print('''
this is akash ghosh
this is akash ghosh
this is akash ghosh
''')

# pyttsx3 modules used for text to speech--------------
import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# os modules used for operating system----------------
import os

directory_path = "/home/krg/Desktop/PYTHONYT/pythonYT/"

contents = os.listdir(directory_path)
print(contents)