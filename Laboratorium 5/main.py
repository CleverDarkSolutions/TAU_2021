from flask import Flask, jsonify, request

app = Flask(__name__)

# Mocked data for /animals endpoint
animals = [
    {'id': 1, 'name': 'Dog', 'type': 'Mammal'},
    {'id': 2, 'name': 'Cat', 'type': 'Mammal'},
    {'id': 3, 'name': 'Fish', 'type': 'Fish'},
    {'id': 4, 'name': 'Turtle', 'type': 'Reptile'},
    {'id': 5, 'name': 'Giraffe', 'type': 'Mammal'}
]

# Mocked data for /weather endpoint
weather = [
    {'id': 1, 'city': 'New York', 'temperature': 10, 'description': 'Cloudy'},
    {'id': 2, 'city': 'Los Angeles', 'temperature': 20, 'description': 'Sunny'},
    {'id': 3, 'city': 'Chicago', 'temperature': -5, 'description': 'Snowy'}
]

# /animals endpoint
@app.route('/animals', methods=['GET'])
def get_animals():
    response = jsonify(animals)
    return response

# /animals/:id endpoint
@app.route('/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = [animal for animal in animals if animal['id'] == animal_id]
    if len(animal) == 0:
        abort(404)
    return jsonify(animal[0])

# /animals endpoint with query parameter
@app.route('/animals', methods=['POST'])
def create_animal():
    if not request.json or not 'name' in request.json:
        abort(400)
    animal = {
        'id': animals[-1]['id'] + 1,
        'name': request.json['name'],
        'type': request.json.get('type', '')
    }
    animals.append(animal)
    return jsonify(animal), 201

# /weather endpoint
@app.route('/weather', methods=['GET'])
def get_weather():
    response = jsonify(weather)
    return response

# /weather/:id endpoint
@app.route('/weather/<int:weather_id>', methods=['GET'])
def get_city_weather(weather_id):
    city_weather = [city_weather for city_weather in weather if city_weather['id'] == weather_id]
    if len(city_weather) == 0:
        abort(404)
    return jsonify(city_weather[0])

if __name__ == '__main__':
    app.run()