# from flask import Flask, request, jsonify
# import requests
# from bs4 import BeautifulSoup
# from prompting.prompts import generate_cohere_summary  # Import the Cohere function

# app = Flask(__name__)

# @app.route('/api/scrape', methods=['POST'])
# def scrape_url():
#     data = request.get_json()
#     url = data['url']
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         text = soup.get_text()
        
#         # Use the Cohere API to generate a summary
#         summary = generate_cohere_summary(text)
        
#         return jsonify({'summary': summary})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from prompting.prompts import generate_cohere_summary  # Import the Cohere function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the TLDR API. Use the /api/scrape endpoint to get a summary."

@app.route('/api/scrape', methods=['POST'])
def scrape_url():
    if request.is_json:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            
            # Use the Cohere API to generate a summary
            summary = generate_cohere_summary(text)
            
            return jsonify({'summary': summary})
        except requests.exceptions.RequestException as e:
            return jsonify({'error': f'Error fetching URL: {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

if __name__ == '__main__':
    app.run(debug=True)
