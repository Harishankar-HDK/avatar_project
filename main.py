# main.py
from stt2 import get_user_input
from tts3 import text_to_speech
from model1 import get_model_response

# Main loop for conversation
def main():
    while True:
        # Step 1: Get user input through speech-to-text
        user_input = get_user_input()
        
        if user_input:
            # Step 2: Get AI model response
            response = get_model_response(user_input)
            print("AI Response:", response)
            
            # Step 3: Convert AI response to speech
            text_to_speech(response)

if __name__ == "__main__":
    main()
