# importing modules
from multiprocessing.connection import Listener
import speech_recognition as sprc
import pyttsx3 
import pyjokes 

#making the speech recognizer + voice speech_engine
listener = sprc.Recognizer()
speech_engine = pyttsx3.init()
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[1].id)

# finding the date and time for greetings
from datetime import datetime 

time = datetime.now()

currentTime = time.strftime("%H")
currentTime = int(currentTime)

afternoon = [12, 13, 14, 15, 16, 17]
evening = [18, 19, 20, 21, 22, 23]
morning = [24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if currentTime in afternoon:
    speech_engine.say("Hello, Good afternoon")
    speech_engine.runAndWait()
elif currentTime in evening:
    speech_engine.say("Hello, Good evening")
    speech_engine.runAndWait()
elif currentTime in morning:
    speech_engine.say("Hello, Good morning")
    speech_engine.runAndWait()

# basic function for saying something  
def talk(text):
    speech_engine.say(text)
    speech_engine.runAndWait()
    print(text)

# listen to speech
def take_command():
    try:
        with sprc.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
        
    except:
        pass 
    return command

# doing the action after the speech
def run_bot():
    command = take_command()
    if 'how are you' in command:
        talk('I am fine, thank you for asking')
    elif 'your name' in command:
        talk('i dont have a name')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else: 
        talk('sorry, i can not help you with this')
    # written in format of 
    # elif 'text' in command:
    # talk('text')

while True:
    run_bot()