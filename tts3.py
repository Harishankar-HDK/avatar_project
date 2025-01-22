from gtts import gTTS
import os
import time
import pygame

def text_to_speech(text):
    # Split the text into smaller chunks (sentences or phrases)
    sentences = text.split(". ") 

    for sentence in sentences:
        # Generate speech for each sentence
        tts = gTTS(text=sentence, lang='en', slow=True) 
        tts.save("response.mp3") 

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("response.mp3")

        # Play the audio
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Stop the mixer
        pygame.mixer.quit()

        # Wait before the next sentence is spoken
        time.sleep(1)