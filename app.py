import pygame
import os

# Init mixer
pygame.mixer.init() #initializes the pygame mixer, for using play and pause commands

songsfolder = "songs"
playlist = [f for f in os.listdir(songsfolder) if f.endswith(".mp3")]
current = 0 #current index of the song from playlist.

def play_song(index):
    pygame.mixer.music.load(os.path.join(songsfolder, playlist[index]))
    pygame.mixer.music.play()
    print(f"Now playing: {playlist[index]}")

play_song(current) # plays the first song

while True:

    command = input("Enter command (next/previous/pause/resume/stop/exit): ").lower()

    if command == "pause":
        pygame.mixer.music.pause()
    elif command == "resume":
        pygame.mixer.music.unpause()
    elif command == "next":
        current = (current+1) % len(playlist)
        play_song(current)
    elif command == "previous":
        current = (current-1) % len(playlist)
        play_song(current)
    elif command == "stop":
        pygame.mixer.music.stop()
    elif command == "exit":
        pygame.mixer.music.stop()
        break
    else:
        print("Invalid command, Try again.")


