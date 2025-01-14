from gtts import gTTS
import os
import time

def text_to_speech(text):
    # Split the text into smaller chunks (sentences or phrases)
    sentences = text.split(". ")  # Split based on periods
    for sentence in sentences:
        # Generate speech for each sentence
        tts = gTTS(text=sentence, lang='en', slow=True)
        tts.save("response.mp3")
        os.system("start response.mp3")
        
        # Wait before the next sentence is spoken
        time.sleep(1)  # Adjust time as necessary (pause between sentences)
