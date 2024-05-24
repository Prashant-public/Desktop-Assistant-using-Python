import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os


# # Taking voice from my system
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)

# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 150)

# def speak(text):
#     '''
#     This function takes string and returns voice

#     Args:
#     text(_type_): String
#     '''
#     engine.say(text)
#     engine.runAndWait()


# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

#open you tube
def open_youtube():
    webbrowser.open('youtube.com')

#open google
def open_google():
    webbrowser.open('google.com')


if __name__ == "__main__":
     open_google()

#query = takeCommand().lower
