import pygame
import os
import speech_recognition as sr

import time
time.sleep(0.2) # adds a short pause for transitioning.

from gtts import gTTS
from playsound import playsound
import tempfile

# Init mixer
pygame.mixer.init() #initializes the pygame mixer, for using play and pause commands

songsfolder = "songs"
playlist = [f for f in os.listdir(songsfolder) if f.endswith(".mp3")]
current = 0 #current index of the song from playlist.
volume = 0.6  # Default volume (60%)
pygame.mixer.music.set_volume(volume)


def speak(text):
    print("🔊 " + text)
    tts = gTTS(text)
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    temp_file.close()  # Close so playsound can access it

    try:
        playsound(temp_file.name)
    finally:
        os.remove(temp_file.name)  # Clean up after speaking


def play_song(index):
    song = playlist[index]
    speak(f"Now playing: {song}")
    time.sleep(0.2)
    pygame.mixer.music.load(os.path.join(songsfolder, song))
    pygame.mixer.music.play()

def get_voice_command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening..")
        r.adjust_for_ambient_noise(source, duration=0.5)  # helps avoid noise interference
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
        is_paused = True
        speak("Music paused.")

    elif "hello" in command:
        speak("Hey boss, I can hear you.")

    elif "increase volume by 1" in command:
        if volume < 1.0:
            volume = min(volume + 0.2, 1.0)
            pygame.mixer.music.set_volume(volume)
            speak("Volume increased by one level.")
        else:
            speak("Volume is already at maximum.")

    elif "decrease volume by 1" in command:
        if volume > 0.0:
            volume = max(volume - 0.2, 0.0)
            pygame.mixer.music.set_volume(volume)
            speak("Volume decreased by one level.")
        else:
            speak("Volume is already at minimum.")

    
    elif "resume" in command or "play" in command:
        if is_paused:
            pygame.mixer.music.unpause()
            speak("Resuming music.")
            is_paused = False
        else:
            speak("Nothing to resume.")

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


