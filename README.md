
# Voice Controlled Music Player

A Python-based voice-driven music player that plays local `.mp3` files, responds to voice commands, and displays song metadata.

## Features

- Voice commands: play, pause, resume, skip, go back, stop, and exit
- Text-to-speech feedback confirming commands and current playing song
- Local music playback with smooth transitions
- Displays song metadata and album art using Mutagen and Tkinter
- Volume control through voice commands
- Modular and extensible code structure

## Technology Stack

- Python 3.8+
- pygame (music playback)
- SpeechRecognition (voice command input)
- PyAudio (microphone interface)
- gTTS (text-to-speech synthesis)
- mutagen (MP3 metadata extraction)
- Tkinter (GUI elements for metadata and album art)

## Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/voice-controlled-music-player.git
   cd voice-controlled-music-player
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your `.mp3` files into the `songs` directory.

4. Run the application:

   ```bash
   python app.py
   ```

The program listens for voice commands such as “play,” “pause,” “next,” “stop,” and “show song info.”

## Example Voice Commands

- Play next song
- Pause
- Resume
- Increase volume by 1
- Show song info
- Stop or exit

## Development Log

- Day 0.0: Integrated libraries (pygame, SpeechRecognition, PyAudio).
- Day 0.1: Implemented basic voice-to-music control loop.
- Day 0.2: Added speech feedback via gTTS.
- Day 0.3: Added song metadata display with Mutagen/Tkinter.
- Day 1.0: Planned GUI dashboard and online music API integration.

## Future Plans

- Develop an interactive GUI dashboard.
- Add support for online music APIs (Spotify, YouTube Music).
- Extend voice command capabilities.
- Improve error handling and edge case management.

## References

- [GeeksforGeeks Python Music Player Guide](https://www.geeksforgeeks.org/python/build-a-music-player-with-tkinter-and-pygame-in-python/)
- [Voice Controlled Music Player Tutorial (YouTube)](https://www.youtube.com/watch?v=h1GmtEo5pwU)
- [DEV Community: How to Build a Music Player](https://dev.to/spiff/build-a-music-player-with-python-3pd2)

## License

This project is licensed under the MIT License.

***
