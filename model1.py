# model.py
import google.generativeai as genai

# Configure the AI model
api_key = "AIzaSyAXAXSbkuJqC8GJGW1AqTfvWcrK2LrW_Zw"
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to generate response from AI model
def get_model_response(user_input):
    try:
        response = model.generate_content(user_input)  # You can adjust the temperature for creativity
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."
