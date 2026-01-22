#Step1: Setup Audio Recorder using sounddevice
import logging
import speech_recognition as sr
from pydub import AudioSegment
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, duration=10, samplerate=16000):
    """Record audio using sounddevice"""
    try:
        logging.info("Checking audio devices...")
        devices = sd.query_devices()
        logging.info(f"Available audio devices: {devices}")
        
        logging.info(f"Recording for {duration} seconds... Please speak now!")
        
        # Record audio
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
        sd.wait()  # Wait until recording is finished
        
        # Save as WAV file
        wavfile.write(file_path, samplerate, audio_data)
        logging.info(f"Audio recorded and saved to {file_path}")
        return True
    except Exception as e:
        logging.error(f"Recording error: {e}")
        return False

# Step2: Setup Speech to Text-STT Model for Transcription
def transcribe_audio(file_path):
    """Transcribe audio file to text"""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        logging.info("Transcription: %s", text)
        return text
    except sr.UnknownValueError:
        logging.error("Speech recognition could not understand audio")
        return None
    except sr.RequestError as e:
        logging.error("Could not request results from Google Speech Recognition service; %s", e)
        return None

# Main execution - only run when script is executed directly
if __name__ == "__main__":
    # Try to record audio
    if record_audio("patient_query.wav", duration=10):
        # Transcribe the recorded audio
        logging.info("Starting transcription...")
        transcribed_text = transcribe_audio("patient_query.wav")
        if transcribed_text:
            logging.info(f"Patient said: {transcribed_text}")
        else:
            logging.warning("No transcription available")
else:
    logging.error("Failed to record audio. Please check your microphone settings.")