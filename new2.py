import pygame
import time
import pyttsx3
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
import threading

# Initialize Pygame and Text-to-Speech Engine
pygame.init()
engine = pyttsx3.init()

# Adjust Text-to-Speech Settings
rate = engine.getProperty('rate')  # Get the current rate
engine.setProperty('rate', rate - 50)  # Reduce speech rate for better sync
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first available voice

# Load Hugging Face Conversational Model
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Screen dimensions
SCREEN_WIDTH = 800  # Increased screen width
SCREEN_HEIGHT = 600  # Increased screen height

# Create Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Avatar")

# Load avatar and mouth images
mouth_rest = pygame.image.load("mouth_rest.jpg")  # Resting mouth
mouth_a = pygame.image.load("mouth_a.jpg")  # 'A' sound
mouth_e = pygame.image.load("mouth_e.jpg")  # 'E' sound
mouth_i = pygame.image.load("mouth_i.jpg")  # 'I' sound
mouth_o = pygame.image.load("mouth_o.jpg")  # 'O' sound
mouth_u = pygame.image.load("mouth_u.jpg")  # 'U' sound

# Resize images to make them larger
mouth_rest = pygame.transform.scale(mouth_rest, (200, 100))  # Increased size
mouth_a = pygame.transform.scale(mouth_a, (200, 100))
mouth_e = pygame.transform.scale(mouth_e, (200, 100))
mouth_i = pygame.transform.scale(mouth_i, (200, 100))
mouth_o = pygame.transform.scale(mouth_o, (200, 100))
mouth_u = pygame.transform.scale(mouth_u, (200, 100))

# Center the mouth dynamically based on image size
mouth_position = (
    (SCREEN_WIDTH - mouth_rest.get_width()) // 2,
    (SCREEN_HEIGHT - mouth_rest.get_height()) // 2,
)

# Define idle animation
def idle_animation():
    screen.blit(mouth_rest, mouth_position)
    pygame.display.flip()
    time.sleep(0.5)  # Rest for half a second

# Continuous lip-sync animation
def continuous_lip_sync(stop_event):
    phonemes = [("a", 0.2), ("e", 0.2), ("i", 0.2), ("o", 0.2), ("u", 0.2), ("rest", 0.2)]
    while not stop_event.is_set():
        for phoneme, duration in phonemes:
            if stop_event.is_set():  # Stop the animation if the event is set
                break
            if phoneme == "rest":
                screen.blit(mouth_rest, mouth_position)
            elif phoneme == "a":
                screen.blit(mouth_a, mouth_position)
            elif phoneme == "e":
                screen.blit(mouth_e, mouth_position)
            elif phoneme == "i":
                screen.blit(mouth_i, mouth_position)
            elif phoneme == "o":
                screen.blit(mouth_o, mouth_position)
            elif phoneme == "u":
                screen.blit(mouth_u, mouth_position)
            pygame.display.flip()
            time.sleep(duration)

# Convert text to speech and trigger lip animation
def text_to_speech_and_lip_sync(response_text):
    # Create a threading event to stop animation when TTS finishes
    stop_event = threading.Event()

    # Start continuous lip-sync animation in a separate thread
    animation_thread = threading.Thread(target=continuous_lip_sync, args=(stop_event,))
    animation_thread.start()

    # Generate TTS audio (runs in the main thread)
    engine.say(response_text)
    engine.runAndWait()

    # Stop the animation once TTS is complete
    stop_event.set()
    animation_thread.join()

# Speech-to-Text function
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

# Generate a response using Hugging Face model
def generate_response(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    response_ids = model.generate(
        inputs,
        max_length=100,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=2,  # Prevent repeating input
        do_sample=True,          # Add variability to response
        temperature=0.7          # Adjust creativity of response
    )
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background
    idle_animation()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Spacebar to trigger interaction
            user_input = get_user_input()
            print("User said:", user_input)

            # Generate AI response
            response_text = generate_response(user_input)
            print("AI Response:", response_text)

            # Text-to-speech and continuous lip-sync
            text_to_speech_and_lip_sync(response_text)

pygame.quit()
