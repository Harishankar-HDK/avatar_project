import pygame
from stt import get_user_input
from nlp import generate_response
from tts import text_to_speech_and_lip_sync

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800  # Increased screen width
SCREEN_HEIGHT = 600  # Increased screen height

# Create Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Avatar")

# Load avatar and mouth images
from utils import load_mouth_images, idle_animation
mouth_images = load_mouth_images()

# Center the mouth dynamically based on image size
mouth_position = (
    (SCREEN_WIDTH - mouth_images["rest"].get_width()) // 2,
    (SCREEN_HEIGHT - mouth_images["rest"].get_height()) // 2,
)

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background
    idle_animation(screen, mouth_images["rest"], mouth_position)

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
            text_to_speech_and_lip_sync(response_text, screen, mouth_images, mouth_position)

pygame.quit()
