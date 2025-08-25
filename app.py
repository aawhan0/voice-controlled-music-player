import pygame
import os
import speech_recognition as sr
import pyttsx3

# Init mixer
pygame.mixer.init() #initializes the pygame mixer, for using play and pause commands

engine = pyttsx3.init() #initializes the pyttsx3.
engine.setProperty('rate', 160)

songsfolder = "songs"
playlist = [f for f in os.listdir(songsfolder) if f.endswith(".mp3")]
current = 0 #current index of the song from playlist.

def speak(text):
    print("🔊 " + text)
    
    engine.say(text)
    engine.runAndWait()


def play_song(index):
    song = playlist[index]
    pygame.mixer.music.load(os.path.join(songsfolder, song))
    pygame.mixer.music.play()
    speak(f"Now playing: {song}")

def get_voice_command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not undertand the audio.")
    except sr.RequestError:
        print("Could not request results.")
    return ""

play_song(current) # plays the first song

while True:

    command = get_voice_command()

    if "pause" in command:
        pygame.mixer.music.pause()
        speak("Music paused.")
    elif "resume" in command or "play" in command:
        pygame.mixer.music.unpause()
        speak("Resuming music.")
    elif "next" in command:
        current = (current+1) % len(playlist)
        play_song(current)
        # speak("")
    elif "previous" in command or "back" in command:
        current = (current-1) % len(playlist)
        play_song(current)
    elif "stop" in command:
        pygame.mixer.music.stop()
        speak("Stopping music.")        

    elif "exit" in command or "quit" in command:
        pygame.mixer.music.stop()
        speak("Exiting the music player.")
        break
    else:
        print("(Did not catch a valid command.)")


