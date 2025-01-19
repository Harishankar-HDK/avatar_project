import speech_recognition as sr

def get_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "I couldn't understand you."
        except sr.RequestError:
            return "Speech service unavailable."
