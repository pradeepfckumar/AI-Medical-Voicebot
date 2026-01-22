# Step1A: Setup Text to Speech-TTS Model with gtts 
from email.mime import text
import os
from gtts import gTTS
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def text_to_speech_with_gtts(input_text, output_file="response.mp3"):
    try:
        language = 'en'
        logging.info(f"Converting text to speech: {input_text}")
        audioobj = gTTS(text=input_text, lang=language, slow=False)
        audioobj.save(output_file)
        logging.info(f"Audio saved successfully to {output_file}")
        return True
    except Exception as e:
        logging.error(f"Error converting text to speech: {e}")
        logging.info("Attempting alternative TTS method...")
        return False

input_text = "Hi! This is Ai Medical in your Service. How can I help you today?"

# Try gTTS first
if not text_to_speech_with_gtts(input_text, "response_gtts.mp3"):
    # Fallback to pyttsx3 (offline TTS)
    try:
        import pyttsx3
        logging.info("Using pyttsx3 for offline text-to-speech...")
        engine = pyttsx3.init()
        engine.say(input_text)
        engine.runAndWait()
        logging.info("Text-to-speech completed successfully!")
    except ImportError:
        logging.error("pyttsx3 not installed. Please install it with: pipenv install pyttsx3")
    except Exception as e:
        logging.error(f"Error with pyttsx3: {e}")

# Step2: Use Model for Text Output to Voice
import subprocess
import platform
def play_audio(file_path):
    """Play audio file based on the operating system."""
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["afplay", file_path])
        else:  # Linux and others
            subprocess.call(["xdg-open", file_path])
        logging.info(f"Playing audio file: {file_path}")
    except Exception as e:
        logging.error(f"Error playing audio file: {e}")
# Play the audio file
if os.path.exists("response_gtts.mp3"):
    play_audio("response_gtts.mp3")
else:
    logging.warning("Audio file not found")