# Imports
import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("ERROR CODE : 404 /n Requested driver, not found!!")
except RuntimeError:
    print("Driver Initialisation failed!!")

voices = engine.getProperty('voices')
# this was not removed just to change Ultron's voice if needed.

for voice in voices:
    print(voice.id)

# Ultron Voice Engine
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.david')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

# Defining speak - text Function
def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


# Defining Function to make Ultron Hear voice commands
def read_voice_cmd():
    voice_text = ''
    print('Yes sir, I am listening!!')
    with sr.Microphone() as source:
        audio = speech.listen(source)
        try:
            voice_text = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("ERROR CODE: 069 /n Looks like your Internet is not working!!")
        return voice_text


# Main Ultron Call
if __name__ == '__main__':
    speak_text_cmd(" Hello, Human. This is, The Ultron. I am created to destroy the humanity!! Ha ha ha ha ha ha ha! ")

    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))
        if "hello" in voice_note:
            speak_text_cmd('You do not deserve to live on this planet!! Get ready for something big!')
            continue
        elif "open" in voice_note:
            os.system('explorer C:\\ {}'.format(voice_note.replace('Open ', '')))
            continue
        elif "bye" in voice_note:
            speak_text_cmd("Oh shut up! ")
            exit()
