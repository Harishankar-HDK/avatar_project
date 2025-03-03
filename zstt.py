import speech_recognition as sr

# Speech to Text with interruption handling
def get_user_input():
    recognizer = sr.Recognizer()
    user_input = None  # Initialize user_input

    with sr.Microphone() as source:
        print("Listening... Please speak if you wish to interrupt.")

        # Adjust for ambient noise (helps in noisy environments)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            # Listen with a timeout, allowing interruption anytime
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=10)  
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)

        except sr.UnknownValueError:
            print("No speech detected, continuing AI response...")  
            return None  # Return None instead of an error message

        except sr.RequestError as e:
            print(f"Google API error: {e}")
            return None

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    return user_input
