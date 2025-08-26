import pygame
import os
import time
time.sleep(0.2) # adds a short pause for transitioning.
from playback import speak
from gui_utils import show_album_art
from speech_utils import get_voice_command

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from tkinter import messagebox

songsfolder = "songs"
volume = 0.6  # Default volume (60%)

# Init mixer
pygame.mixer.init() #initializes the pygame mixer, for using play and pause commands

playlist = [f for f in os.listdir(songsfolder) if f.endswith(".mp3")]
current = 0 #current index of the song from playlist.
current_metadata = {}
is_paused = False
pygame.mixer.music.set_volume(volume)

def play_song(index):
    global current_song, current_metadata
    song = playlist[index]
    current_song = song

    song_path = os.path.join(songsfolder, song)
    show_album_art(song_path)

    try:
        audio = MP3(song_path, ID3=EasyID3)
        title = audio.get("title", [song])[0]
        artist = audio.get("artist", ["Unknown Artist"])[0]
        duration = int(audio.info.length)
    except Exception:
        title = song
        artist = "Unknown Artist"
        duration = 0

    current_metadata = {
        "title": title,
        "artist": artist,
        "duration": f"{duration //60}: {duration % 60:02d}"
    }

    speak(f"Now playing {title} by {artist}.")
    print(f"🎶 Title: {title}")
    print(f"🎤 Artist: {artist}")
    print(f"⏱️ Duration: {duration // 60}:{duration % 60:02d} minutes")
    
    
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def show_song_info():
    if current_metadata:
        info = (
            f"🎵 Title: {current_metadata['title']}\n"
            f"🎤 Artist: {current_metadata['artist']}\n"
            f"⏱️ Duration: {current_metadata['duration']} mins"
        )

        # Popup window
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showinfo("Now Playing", info)
        root.destroy()
        
        speak(f"You are listening to {current_metadata['title']} by {current_metadata['artist']}.")


play_song(current) # plays the first song

while True:

    command = get_voice_command()

    if "pause" in command:
        pygame.mixer.music.pause()
        is_paused = True
        speak("Music paused.")

    elif "hello" in command:
        speak("Hey boss, I can hear you.")

    elif "what is playing" in command or "show song info" in command or "song details" in command:
        speak(f"You are listening to: {current_song}")
        print(f"🎶 Now playing: {current_song}")

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


