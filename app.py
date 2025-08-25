import pygame
import os

# Init mixer
pygame.mixer.init()

# Load music files
music_folder = "songs"  # Make a folder with some MP3s
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current = 0

def play_song(index):
    pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
    pygame.mixer.music.play()

play_song(current)

while True:
    command = input("Enter command (next/pause/resume/stop/exit): ").lower()
    if command == "pause":
        pygame.mixer.music.pause()
    elif command == "resume":
        pygame.mixer.music.unpause()
    elif command == "next":
        current = (current + 1) % len(playlist)
        play_song(current)
    elif command == "stop":
        pygame.mixer.music.stop()
    elif command == "exit":
        break
