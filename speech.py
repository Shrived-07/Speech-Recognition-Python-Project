import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the source of input
with sr.Microphone() as source:
    print("Please say something:")
    # Listen for the first phrase and extract it into audio data
    audio = r.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
