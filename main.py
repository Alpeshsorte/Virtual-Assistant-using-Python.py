import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# from gtts import gTTS
# import pygame
# import os
recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts=gTTs(text)
#     tts.save('temp.mp3')
#     pygame.mixer.init()
#     pygame.mixer.music.load('temp.mp3')
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.clock().tick(10)
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtubr" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    # else:

    pass

if __name__ == "__main__":
    speak=("Initializing Assistant....")
    while True:
        r=sr.Recognizer()


        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source, timeout=2, phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="Assistant"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Assistant Active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
            # print(command)
        except Exception as e:
            print("Error; {0}".format(e))