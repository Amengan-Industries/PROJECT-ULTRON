# Imports
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

# -----------------------------
speech = sr.Recognizer()
error_occurred = 0
# -----------------------------

# User Commands' Dictionary
greeting_dict = {'hello': 'hello', 'hai': 'hai'}
open_launch_dict = {'open': 'open'}
google_queries_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'when': 'when'}
open_bye_dict = {'bye': 'bye'}
play_music_dict = {'motivational': 'motivational', 'rocking': 'rocking'}

# URLs' Dictionary
social_media_dict = {'instagram': "https://instagram.com/", 'twitter': "https://www.twitter.com/"}

# Ultron TTS's List
mp3_greeting_list = ['UltronVoice/UltronTTS/Greetings02Namaste.mp3', 'UltronVoice/UltronTTS/Askingtask.mp3']
mp3_open_launch_list = ['UltronVoice/UltronTTS/swoosh.mp3', 'UltronVoice/UltronTTS/Opening.mp3']
mp3_google_search_list = ['UltronVoice/UltronTTS/Ultron_search_voice.mp3']
mp3_hearing_turbulence_list = ['UltronVoice/UltronTTS/Ultron_Hearing_turbulence.mp3']
mp3_birth_story = ['UltronVoice/UltronTTS/Birth.mp3']
mp3_sarcastic_reply = ['UltronVoice/UltronTTS/sarcasm.mp3']
mp3_thanks_reply = ['UltronVoice/UltronTTS/thanx_rep.mp3']
mp3_bye_list = ['UltronVoice/UltronTTS/Bye01normal.mp3', 'UltronVoice/UltronTTS/Bye02seeyah.mp3']
mp3_bye_tune = ['UltronVoice/UltronTTS/Ultron_Bye_tune.mp3']

# Defining Function
# Main Function
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


# Input Voice Modification
def read_voice_cmd():
    voice_text = ''
    print('Yes sir, I am listening!!')

    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        # Error Management
        return errormanagement()

    except sr.RequestError:
        print("ERROR CODE: 069 /n Looks like your Internet is not working!!")
    except sr.WaitTimeoutError:
        # Error Management
        return errormanagement()

    return voice_text


# Ultron Error Management
def errormanagement():
    global error_occurred
    if error_occurred == 0:
        play_sound(mp3_hearing_turbulence_list)
    exit()

# Ultron Greet Function
def is_valid_greeting(greet_dict, voice_note):
    for key, value in greet_dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break

        except IndexError:
            pass

    return False


# Ultron Open applications Function
def is_valid_open_launch(open_launch_dict, voice_note):
    for key, value in open_launch_dict.items():
        if value == voice_note.split(' ')[0]:
            return True
        break

    return False


# Ultron Searches Google
def is_valid_google_search(phrase):
    if google_queries_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]:
        return True


# Ultron Social Media Function
def is_valid_social_media(social_media_dict, voice_note):
    for key, value in open_launch_dict.items():
        if value == voice_note.split(' ')[0]:
            return True
        break

    return False


# Ultron Bye Function
def is_valid_bye(open_bye_dict, voice_note):
    for key, value in open_bye_dict.items():
        if value == voice_note.split(' ')[0]:
            return True
        break

    return False


# Function Call
if __name__ == '__main__':
    playsound('UltronVoice/UltronTTS/Ultron_tune.mp3')
    playsound('UltronVoice/UltronTTS/Greetings03Main.mp3')
    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_greeting(greeting_dict, voice_note):
            print('Greeting... ')
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_open_launch(open_launch_dict, voice_note):
            print("Opening... ")
            play_sound(mp3_open_launch_list)
            if is_valid_social_media(social_media_dict, voice_note):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\"{}'.format(voice_note.replace('open', '').replace('launch ', '')))
            continue

        elif "how were you born" in voice_note:
            print("Hmmm... That's how legends are born!!")
            play_sound(mp3_birth_story)
            continue

        elif "thank you" in voice_note:
            print("Thanking me??")
            play_sound(mp3_sarcastic_reply)
            continue

        elif "thankyou ultron" in voice_note:
            print("Pleasure!!")
            play_sound(mp3_thanks_reply)
            continue

        elif is_valid_google_search(voice_note):
            print('Searching...')
            play_sound(mp3_google_search_list)
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            continue

        elif "bye" in voice_note:
            print("Seeyah, have a good day!!")
            play_sound(mp3_bye_list)
            play_sound(mp3_bye_tune)
            exit()
