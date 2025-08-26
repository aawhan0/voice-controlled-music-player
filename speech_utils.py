import speech_recognition as sr

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