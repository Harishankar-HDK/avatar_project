import speech_recognition as sr

# Speech to Text
def get_user_input():
    recognizer = sr.Recognizer()
    user_input = None  # Initialize user_input to None

    with sr.Microphone() as source:
        print("Listening... Please speak.")
        
        # Adjust for ambient noise (optional but helpful in noisy environments)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Listen to the source with a timeout (you can adjust this value)
            audio = recognizer.listen(source, timeout=5)  # Timeout after 5 seconds of silence
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Please speak again.")
        except sr.RequestError as e:
            print(f"There was an issue with the request to Google API: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
    return user_input
