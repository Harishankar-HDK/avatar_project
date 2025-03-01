from stt1 import get_user_input
from tts1 import text_to_speech
from model import get_model_response
from preprocessing import clean_model_output

# Main loop for conversation
def main():
    while True:
        # Step 1: Get user input through speech-to-text
        user_input = get_user_input()
        
        if user_input.lower()!='exit':
            # Step 2: Get AI model response
            response = get_model_response(user_input)

            clean_response=clean_model_output(response)
            print("AI Response:", clean_response)
            text_to_speech(clean_response)
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
