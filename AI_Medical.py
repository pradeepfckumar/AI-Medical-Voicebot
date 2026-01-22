# Step1: Setup Groq API Key
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

Groq_api_key = os.getenv("Groq_api")
print("Groq API Key:", Groq_api_key)

# Set the API key for Groq client
if Groq_api_key:
    os.environ["GROQ_API_KEY"] = Groq_api_key

# Step2: Convert Image to Required Format
import base64

def encode_image_to_base64(image_path):
    image_file = open(image_path, "rb")
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

# Step3: Setup Multimodal LLM
from groq import Groq

def analyze_image_with_query(encoded_image, query):
    """Analyze an image with a medical query using Groq API"""
    try:
        client = Groq()
        model = "meta-llama/llama-4-scout-17b-16e-instruct"
        message = [
            {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": query,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],

            }]

        completion = client.chat.completions.create(
            model=model,
            messages=message    
        )

        response = completion.choices[0].message.content
        print("Response:", response)
        return response
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return f"Error: {str(e)}"