from flask import Flask, render_template, jsonify, abort, make_response, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sanctuaries'
heroku = Heroku(app)
db = SQLAlchemy(app)

sanctuaries = [
    {
        'id': 1,
        'name': 'Hope Haven',
        'animals': [
            {
                'id': 1,
                'name': 'Persephone',
                'events': [
                    {
                        'id': 1,
                        'task': 'teeth cleaning',
                        'due': '1/1/17'
                    },
                    {
                        'id': 2,
                        'task': 'hoof trim',
                        'due': '5/23/17'
                    }
                ]
            },
            {
                'id': 2,
                'name': 'Carl',
                'events': [
                    {
                        'id': 1,
                        'task': 'teeth floating',
                        'due': '1/15/17'
                    },
                    {
                        'id': 2,
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
                'id': 1,
                'name': u'Louis',
                'events': [
                    {
                        'id': 1,
                        'task': u'teeth cleaning',
                        'due': u'5/1/17'
                    },
                    {
                        'id': 2,
                        'task': u'deworming',
                        'due': u'4/23/17'
                    }
                ]
            },
            {
                'id': 2,
                'name': u'Isaac',
                'events': [
                    {
                        'id': 1,
                        'task': u'hoof maintenance',
                        'due': u'1/15/17'
                    },
                    {
                        'id': 2,
                        'task': u'antibiotics',
                        'due': u'4/15/17'
                    }
                ]
            }
        ]
    }
]

# NON-API ROUTES
@app.route('/sanctuary')
@app.route('/')
def index():
    print('hi')
    return render_template('index.html')


# DATABASE
# Create our database models
# SANCTUARY
class Sanctuary(db.Model):
    __tablename__ = "sanctuaries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

# ANIMAL
class Animal(db.Model):
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    # PROBABLY NEED TO CHANGE PRIMARY_KEY
    sanctuaryId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

# EVENT
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    # PROBABLY NEED TO CHANGE PRIMARY_KEY
    animalId = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), unique=True)
    due = db.Column(db.String(120), unique=True)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return '<Task %r>' % self.task

    def __init__(self, due):
        self.due = due

    def __repr__(self):
        return '<Due date %r>' % self.due


# Save sanctuary name to database
@app.route('/sanc', methods=['POST'])
def sanc():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(Sanctuary).filter(Sanctuary.name == name).count():
            reg = Sanctuary(name)
            db.session.add(reg)
            db.session.commit()
            # return render_template('success.html')
    return render_template('index.html')

# Save animal name to database
@app.route('/animal', methods=['POST'])
def animal():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # Check that animal does not already exist (not a great query, but works)
        if not db.session.query(Animal).filter(Animal.name == name).count():
            reg = Animal(name)
            db.session.add(reg)
            db.session.commit()
            # return render_template('success.html')
    return render_template('index.html')

# Save event task and due date to database
@app.route('/task', methods=['POST'])
def task():
    task = None
    due = None
    if request.method == 'POST':
        task = request.form['task']
        due = request.form['due']
        # Check that task does not already exist (not a great query, but works)
        if not db.session.query(Event).filter(Event.task == task).count():
            reg_task = Event(task)
            reg_due = Event(due)
            db.session.add(reg_task)
            db.session.add(reg_due)
            db.session.commit()
            # return render_template('success.html')
    return render_template('index.html')

# Edit event task or due date - I strongly feel this is wrong.
@app.route('/edittask', methods=['PUT'])
def edittask():
    task = None
    due = None
    if request.method == 'PUT':
        task = request.form['task']
        due = request.form['due']
        # Check that task already exists (not a great query, but works)
        if db.session.query(Event).filter(Event.task == task).count():
            reg_task = Event(task)
            reg_due = Event(due)
            db.session.add(reg_task)
            db.session.add(reg_due)
            db.session.commit()
            # return render_template('success.html')
    return render_template('index.html')

# Delete event task and due date - no clue how to do this.
@app.route('/deletetask', methods=['DELETE'])
def deletetask():
    task = None
    due = None
    if request.method == 'PUT':
        task = request.form['task']
        due = request.form['due']
        # Check that task already exists (not a great query, but works)
        if db.session.query(Event).filter(Event.task == task).count():
            reg_task = Event(task)
            reg_due = Event(due)
            db.session.add(reg_task)
            db.session.add(reg_due)
            db.session.commit()
            # return render_template('success.html')
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


# ANIMALS
animals = sanctuaries[0]['animals']

@app.route('/sanctuary/api/animals', methods=['GET'])
def get_animals():
    return jsonify({'animals': [make_public_animal(animal) for animal in animals]})

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = [animal for animal in animals if animal['id'] == animal_id]
    if len(animal) == 0:
        abort(404)
    return jsonify({'animal': animal[0]})

@app.route('/sanctuary/api/animals', methods=['POST'])
def create_animal():
    if not request.json or not 'name' in request.json:
        abort(400)
    animal = {
        'id': animals[-1]['id'] + 1,
        'name': request.json['name'],
    }
    animals.append(animal)
    return jsonify({'animal': animal}), 201

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = [animal for animal in animals if animal['id'] == animal_id]
    if len(animal) == 0:
        abort(404)
    animals.remove(animal[0])
    return jsonify({'result': True})

def make_public_animal(animal):
    new_animal = {}
    for field in animal:
        if field == 'id':
            new_animal['uri'] = url_for('get_animal', animal_id=animal['id'], _external=True)
        new_animal[field] = animal[field]
    return new_animal

# EVENTS
events = sanctuaries[0]['animals'][0]['events']

# Add int:animal_id
@app.route('/sanctuary/api/events', methods=['GET'])
def get_events():
    return jsonify({'events': [make_public_event(event) for event in events]})

@app.route('/sanctuary/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = [event for event in events if event['id'] == event_id]
    if len(event) == 0:
        abort(404)
    return jsonify({'event': event[0]})

@app.route('/sanctuary/api/events', methods=['POST'])
def create_event():
    if not request.json or not 'task' in request.json:
        abort(400)
    event = {
        'id': events[-1]['id'] + 1,
        'task': request.json['task'],
    }
    events.append(event)
    return jsonify({'event': event}), 201

@app.route('/sanctuary/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = [event for event in events if event['id'] == event_id]
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
    event = [event for event in events if event['id'] == event_id]
    if len(event) == 0:
        abort(404)
    events.remove(event[0])
    return jsonify({'result': True})

def make_public_event(event):
    new_event = {}
    for field in event:
        if field == 'id':
            new_event['uri'] = url_for('get_event', event_id=event['id'], _external=True)
        new_event[field] = event[field]
    return new_event

if __name__ == '__main__':
  app.run(debug=True)
