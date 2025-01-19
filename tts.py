import pyttsx3
import threading
import time
import pygame

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Adjust Text-to-Speech Settings
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def text_to_speech_and_lip_sync(response_text, screen, mouth_images, mouth_position):
    stop_event = threading.Event()

    # Lip-sync animation
    def continuous_lip_sync():
        phonemes = [("a", 0.2), ("e", 0.2), ("i", 0.2), ("o", 0.2), ("u", 0.2), ("rest", 0.2)]
        while not stop_event.is_set():
            for phoneme, duration in phonemes:
                if stop_event.is_set():
                    break
                screen.blit(mouth_images[phoneme], mouth_position)
                pygame.display.flip()
                time.sleep(duration)

    animation_thread = threading.Thread(target=continuous_lip_sync)
    animation_thread.start()

    # Text-to-speech
    engine.say(response_text)
    engine.runAndWait()

    # Stop animation
    stop_event.set()
    animation_thread.join()
