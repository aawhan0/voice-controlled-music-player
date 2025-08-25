# voice-controlled-music-player
Voice controlled music player using python libraries.

Day 0.0: Starting with learning about the libraries required in this project:
1. SpeechRecognition - converts the input voice to text.
2. PyAudio - deals with input output handling at the same time.
3. Pygame - provides an interface.

Day 0.1: The basic app is now created.

Function: Reads the local .mp3 stored within the directory, and takes your microphone's input -> converts it into text -> interprets the text accordingly inside the while loop.

Day 0.2: Making the app speak back.

I tried using pyttsx3 (text to speech library) but it doesnt help, as it keeps on crasing and messes up with the while loop. So I am now going to try using gTTs + playsound.
