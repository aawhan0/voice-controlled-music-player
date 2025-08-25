import pygame
import os
import speech_recognition as sr

# Init mixer
pygame.mixer.init() #initializes the pygame mixer, for using play and pause commands

songsfolder = "songs"
playlist = [f for f in os.listdir(songsfolder) if f.endswith(".mp3")]
current = 0 #current index of the song from playlist.

def play_song(index):
    pygame.mixer.music.load(os.path.join(songsfolder, playlist[index]))
    pygame.mixer.music.play()
    print(f"Now playing: {playlist[index]}")

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
    elif "resume" in command or "play" in command:
        pygame.mixer.music.unpause()
    elif "next" in command:
        current = (current+1) % len(playlist)
        play_song(current)
    elif "previous" in command or "back" in command:
        current = (current-1) % len(playlist)
        play_song(current)
    elif "stop" in command:
        pygame.mixer.music.stop()
    elif "exit" in command or "quit" in command:
        pygame.mixer.music.stop()
        break
    else:
        print("Did not catch a valid command.")


