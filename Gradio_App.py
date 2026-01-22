# Voicebot UI with Gradio
import os
import gradio as gr
import logging
from AI_Medical import encode_image_to_base64, analyze_image_with_query
from Patient_Voice import transcribe_audio
from Doctor_Voice import text_to_speech_with_gtts

logging.basicConfig(level=logging.INFO)

def process_input(audio_file, image_file):
    """Process audio and image input to generate medical response"""
    try:
        # Step 1: Transcribe audio
        if not audio_file:
            return "No audio provided", "No medical response", None
        
        speech_to_text_output = transcribe_audio(audio_file)
        if not speech_to_text_output:      
            return "No speech detected", "No medical response", None
        
        logging.info(f"Transcribed: {speech_to_text_output}")
        
        # Step 2: Analyze the image if provided
        ai_medical_response = "No image provided"
        if image_file:
            image_base64 = encode_image_to_base64(image_file)
            ai_medical_response = analyze_image_with_query(image_base64, speech_to_text_output)
            logging.info(f"AI Response: {ai_medical_response}")

        # Step 3: Convert AI response to speech
        text_to_speech_with_gtts(ai_medical_response, "doctor_response.mp3")

        return speech_to_text_output, ai_medical_response, "doctor_response.mp3"
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        logging.error(error_msg)
        return error_msg, "Processing failed", None

# Create the Interface
iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Audio(sources="microphone", type="filepath", label="Record your query"),
        gr.Image(type="filepath", label="Upload an image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="AI Medical Response"),
        gr.Audio(label="Text to Speech Response")
    ],
    title="AI Medical Voicebot",
    description="Record your medical query and upload an image for analysis."
)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🏥 AI Medical Voicebot is starting...")
    print("="*60)
    print("\n✅ Your app is running!")
    print("📱 Access it from your computer at: http://localhost:7861")
    print("🌐 To share with others, use your IP address:\n")
    iface.launch(
        debug=True, 
        share=False,
        server_name="0.0.0.0",
        server_port=7861,
        show_error=True
    )