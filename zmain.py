from zstt import get_user_input
from ztts1 import text_to_speech, stop_audio
from zmodel import get_model_response
from zpreprocessing import clean_model_output
import threading
import sys  # Import sys for forceful exit

def main():
    speaking_thread = None  

    while True:
        user_input = get_user_input()

        if user_input and user_input.lower() == 'exit':
            print("Goodbye!")
            stop_audio()  # Stop any ongoing speech
            if speaking_thread and speaking_thread.is_alive():
                speaking_thread.join()  # Ensure speech thread exits
            sys.exit(0)  # Forcefully exit the program

        # If AI is speaking, stop it before continuing
        if speaking_thread and speaking_thread.is_alive():
            if user_input:
                stop_audio()  
                speaking_thread.join()
            else:
                continue  

        if user_input:  
            response = get_model_response(user_input)
            clean_response = clean_model_output(response)
            print("AI Response:", clean_response)

            # Start speaking immediately without delay
            speaking_thread = text_to_speech(clean_response)

if __name__ == "__main__":
    main()
