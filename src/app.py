from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def generate_summary(text):
    # Placeholder function for summary generation
    return ' '.join(text.split()[:50]) + '...'

@app.route('/api/scrape', methods=['POST'])
def scrape_url():
    data = request.get_json()
    url = data['url']
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        summary = generate_summary(text)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
