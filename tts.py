import threading
import time
import pygame
from gtts import gTTS
import os

# Initialize pygame mixer for audio playback
pygame.mixer.init()

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

    # Start the animation thread
    animation_thread = threading.Thread(target=continuous_lip_sync)
    animation_thread.start()

    # Convert text to speech and save to file
    tts = gTTS(text=response_text, lang='en')
    audio_file = "response.mp3"
    tts.save(audio_file)

    try:
        # Load and play the audio using pygame.mixer
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Stop and unload the music to release the file
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    except pygame.error as e:
        print(f"Error playing sound: {e}")

    finally:
        # Stop the animation
        stop_event.set()
        animation_thread.join()

        # Cleanup: Remove the audio file after playback
        if os.path.exists(audio_file):
            try:
                os.remove(audio_file)
            except PermissionError:
                print(f"Unable to delete {audio_file}. It may still be in use.")

