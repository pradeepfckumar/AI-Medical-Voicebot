# 🏥 AI Medical Voicebot

**👤 Portfolio Project by:** [Your Name]  
**📄 View My Resume:** [Link to your resume or portfolio]  
**💼 GitHub:** [Your GitHub profile link]

---

## Quick Start

### To Run the Application:
1. **Double-click** `START_APP.bat` (Windows)
2. Wait for the server to start
3. Open browser to: **http://127.0.0.1:7860**

---

## 📋 How to Use

1. **Record Query**: Click the microphone icon and speak your medical question
2. **Upload Image**: Select a medical image to analyze (optional)
3. **Get Analysis**: The AI will:
   - Transcribe your speech to text
   - Analyze the image if provided
   - Generate a medical response
   - Convert response to speech

---

## 🔗 Access Points

### Local Machine:
```
http://127.0.0.1:7860
```

### Same Network (from another computer):
```
http://<YOUR_COMPUTER_IP>:7860
```
*Replace `<YOUR_COMPUTER_IP>` with your computer's IP address*

---

## 📝 Features

✅ **Voice Recording** - Record patient questions
✅ **Speech-to-Text** - Transcribe audio to text
✅ **Image Analysis** - Analyze medical images with AI
✅ **Text-to-Speech** - Convert responses to audio
✅ **Web Interface** - User-friendly Gradio UI

---

## 🛠️ System Requirements

- Python 3.14+
- Windows/macOS/Linux
- Microphone (for voice recording)
- Internet connection (for Groq API)

---

## 📁 Project Files

- `Gradio_App.py` - Main web interface
- `AI_Medical.py` - Medical image analysis
- `Patient_Voice.py` - Audio recording & transcription
- `Doctor_Voice.py` - Text-to-speech responses
- `START_APP.bat` - Quick launcher (Windows)

---

## 🚀 Development Notes

The application uses:
- **Groq API** - Vision-language model for medical analysis
- **Gradio** - Web interface
- **SpeechRecognition** - Audio transcription
- **gTTS** - Text-to-speech conversion

---

**Created:** January 22, 2026
**Status:** ✅ Fully Functional
