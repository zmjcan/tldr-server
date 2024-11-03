from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from prompting.prompts import generate_cohere_summary  # Import the Cohere function

app = Flask(__name__)

@app.route('/api/scrape', methods=['POST'])
def scrape_url():
    data = request.get_json()
    url = data['url']
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        # Use the Cohere API to generate a summary
        summary = generate_cohere_summary(text)
        
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)