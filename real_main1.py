import threading
from stt2 import recognize_speech
from tts1 import text_to_speech
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load fine-tuned model
model_name = "C:/Users/user/Desktop/Ai_avatar_project/fine_tuned_model"  # Path to your fine-tuned model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate AI response
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Play response in a separate thread
def play_response(response):
    text_to_speech(response)

def main():
    print("AI Companion is ready! Say something or type 'exit' to quit.")

    while True:
        print("\nListening...")
        user_input = recognize_speech()

        if user_input:
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Generate response
            response = generate_response(user_input)
            print(f"AI Response: {response}")

            # Speak the response
            threading.Thread(target=play_response, args=(response,)).start()

if __name__ == "__main__":
    main()
