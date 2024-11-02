import cohere
import json
import os
from apikey import COHERE_API_KEY

# Configure Cohere API key
cohere_client = cohere.Client(COHERE_API_KEY)

URL = "<URL>"
TAILOR_PROMPT = """Consider the following url: <URL>
Your task is to summarize the text in the URL in 50 words:
"""

def generate_cohere_summary(text):
    response = cohere_client.generate(
        model='xlarge',  # Specify the model you want to use
        prompt=TAILOR_PROMPT.replace("<URL>", text),
        max_tokens=100,  # Adjust max tokens according to your needs
        temperature=0.5,  # Control randomness
    )
    return clean_response(response.generations[0].text)

def clean_response(response_text):
    response_text = response_text.replace('```json\n', '').replace('\n```', '')
    response_text = response_text.replace('●', '').strip()
    return response_text
