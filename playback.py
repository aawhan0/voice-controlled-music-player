import pygame
from gtts import gTTS
from playsound import playsound
import tempfile
import os


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

