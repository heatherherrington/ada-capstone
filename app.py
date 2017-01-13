from flask import Flask, render_template, jsonify, abort, make_response, request, url_for
app = Flask(__name__)

sanctuaries = [
    {
        'sanctuaryId': 1,
        'name': 'Hope Haven',
        'animals': [
            {
                'animalId': 1,
                'name': 'Persephone',
                'events': [
                    {
                        'eventId': 1,
                        'task': 'teeth cleaning',
                        'due': '1/1/17'
                    },
                    {
                        'eventId': 2,
                        'task': 'hoof trim',
                        'due': '5/23/17'
                    }
                ]
            },
            {
                'animalId': 2,
                'name': 'Carl',
                'events': [
                    {
                        'eventId': 1,
                        'task': 'teeth floating',
                        'due': '1/15/17'
                    },
                    {
                        'eventId': 2,
                        'task': 'deworm',
                        'due': '4/23/17'
                    }
                ]
            }
        ]
    },
    {
        'sanctuaryId': 2,
        'name': u'Farm Friends',
        'animals': [
            {
                'animalId': 1,
                'name': u'Louis',
                'events': [
                    {
                        'eventId': 1,
                        'task': u'teeth cleaning',
                        'due': u'5/1/17'
                    },
                    {
                        'eventId': 2,
                        'task': u'deworming',
                        'due': u'4/23/17'
                    }
                ]
            },
            {
                'animalId': 2,
                'name': u'Isaac',
                'events': [
                    {
                        'eventId': 1,
                        'task': u'hoof maintenance',
                        'due': u'1/15/17'
                    },
                    {
                        'eventId': 2,
                        'task': u'antibiotics',
                        'due': u'4/15/17'
                    }
                ]
            }
        ]
    }
]

# NON-API ROUTES

@app.route('/')
def index():
    print('hi')
    return render_template('index.html')

# API

# SANCTUARIES

@app.route('/sanctuary/api/sanctuaries', methods=['GET'])
def get_sanctuaries():
    return jsonify({'sanctuaries': [make_public_sanctuary(sanctuary) for sanctuary in sanctuaries]})

@app.route('/sanctuary/api/sanctuaries/<int:sanctuary_id>', methods=['GET'])
def get_sanctuary(sanctuary_id):
    sanctuary = [sanctuary for sanctuary in sanctuaries if sanctuary['sanctuaryId'] == sanctuary_id]
    if len(sanctuary) == 0:
        abort(404)
    return jsonify({'sanctuary': sanctuary[0]})

@app.route('/sanctuary/api/sanctuaries', methods=['POST'])
def create_sanctuary():
    if not request.json or not 'name' in request.json:
        abort(400)
    sanctuary = {
        'sanctuaryId': sanctuaries[-1]['sanctuaryId'] + 1,
        'name': request.json['name'],
    }
    sanctuaries.append(sanctuary)
    return jsonify({'sanctuary': sanctuary}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_sanctuary(sanctuary):
    new_sanctuary = {}
    for field in sanctuary:
        if field == 'sanctuaryId':
            new_sanctuary['uri'] = url_for('get_sanctuary', sanctuary_id=sanctuary['sanctuaryId'], _external=True)
        new_sanctuary[field] = sanctuary[field]
    return new_sanctuary


# ANIMALS - Need 'DELETE'
animals = sanctuaries[0]['animals']

@app.route('/sanctuary/api/animals', methods=['GET'])
def get_animals():
    return jsonify({'animals': [make_public_animal(animal) for animal in animals]})

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = [animal for animal in animals if animal['animalId'] == animal_id]
    if len(animal) == 0:
        abort(404)
    return jsonify({'animal': animal[0]})

@app.route('/sanctuary/api/animals', methods=['POST'])
def create_animal():
    if not request.json or not 'name' in request.json:
        abort(400)
    animal = {
        'animalId': animals[-1]['animalId'] + 1,
        'name': request.json['name'],
    }
    animals.append(animal)
    return jsonify({'animal': animal}), 201

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = [animal for animal in animals if animal['animalId'] == animal_id]
    if len(animal) == 0:
        abort(404)
    animals.remove(animal[0])
    return jsonify({'result': True})

def make_public_animal(animal):
    new_animal = {}
    for field in animal:
        if field == 'animalId':
            new_animal['uri'] = url_for('get_animal', animal_id=animal['animalId'], _external=True)
        new_animal[field] = animal[field]
    return new_animal

# EVENTS - Need 'PUT', 'DELETE'
events = sanctuaries[0]['animals'][0]['events']

@app.route('/sanctuary/api/events', methods=['GET'])
def get_events():
    return jsonify({'events': [make_public_event(event) for event in events]})

@app.route('/sanctuary/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = [event for event in events if event['eventId'] == event_id]
    if len(event) == 0:
        abort(404)
    return jsonify({'event': event[0]})

@app.route('/sanctuary/api/events', methods=['POST'])
def create_event():
    if not request.json or not 'task' in request.json:
        abort(400)
    event = {
        'eventId': events[-1]['eventId'] + 1,
        'task': request.json['task'],
    }
    events.append(event)
    return jsonify({'event': event}), 201

@app.route('/sanctuary/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = [event for event in events if event['eventId'] == event_id]
    if len(event) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'task' in request.json and type(request.json['task']) != unicode:
        abort(400)
    if 'due' in request.json and type(request.json['due']) is not unicode:
        abort(400)
    event[0]['task'] = request.json.get('task', event[0]['task'])
    event[0]['due'] = request.json.get('due', event[0]['due'])
    return jsonify({'event': event[0]})

@app.route('/sanctuary/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = [event for event in events if event['eventId'] == event_id]
    if len(event) == 0:
        abort(404)
    events.remove(event[0])
    return jsonify({'result': True})

def make_public_event(event):
    new_event = {}
    for field in event:
        if field == 'eventId':
            new_event['uri'] = url_for('get_event', event_id=event['eventId'], _external=True)
        new_event[field] = event[field]
    return new_event

if __name__ == '__main__':
  app.run(debug=True)
