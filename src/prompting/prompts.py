import cohere
import os
from apikey import COHERE_API_KEY

# Configure Cohere API key
cohere_client = cohere.Client(COHERE_API_KEY)

TAILOR_PROMPT = """Consider the following text:
{text}

Your task is to summarize the text above in 50 words.
"""

def generate_cohere_summary(text):
    try:
        response = cohere_client.generate(
            model='command-xlarge-nightly',  # Use a valid model identifier
            prompt=TAILOR_PROMPT.format(text=text[:4000]),  # Use the first 4000 characters
            max_tokens=100,  # Adjust max tokens according to your needs
            temperature=0.5,  # Control randomness
        )
        return clean_response(response.generations[0].text)
    except cohere.CohereError as e:
        return f"An error occurred while generating summary: {str(e)}"

def clean_response(response_text):
    response_text = response_text.replace('```json\n', '').replace('\n```', '')
    response_text = response_text.replace('●', '').strip()
    return response_text

