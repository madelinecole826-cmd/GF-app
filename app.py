from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/gluten_free_restaurants', methods=['GET'])
def gluten_free_restaurants():
    location = request.args.get('location')
    api_key = 'YOUR_GOOGLE_PLACES_API_KEY'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query=gluten+free+restaurants+in+{location}&key={api_key}'

    response = requests.get(url)
    results = response.json().get('results', [])

    restaurants = [{'name': place['name'], 'address': place['formatted_address']} for place in results]

    return jsonify(restaurants)

if __name__ == '__main__':
    app.run(debug=True)