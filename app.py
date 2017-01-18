from flask import Flask, render_template, jsonify, abort, make_response, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sanctuaries'
heroku = Heroku(app)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# sanctuaries = [
#     {
#         'id': 1,
#         'name': 'Hope Haven',
#         'animals': [
#             {
#                 'id': 1,
#                 'name': 'Finn',
#                 'events': [
#                     {
#                         'id': 1,
#                         'task': 'teeth cleaning',
#                         'due': '1/1/17'
#                     },
#                     {
#                         'id': 2,
#                         'task': 'hoof trim',
#                         'due': '5/23/17'
#                     }
#                 ]
#             },
#             {
#                 'id': 2,
#                 'name': 'Carl',
#                 'events': [
#                     {
#                         'id': 3,
#                         'task': 'teeth floating',
#                         'due': '1/15/17'
#                     },
#                     {
#                         'id': 4,
#                         'task': 'deworm',
#                         'due': '4/23/17'
#                     }
#                 ]
#             }
#         ]
#     },
#     {
#         'sanctuaryId': 2,
#         'name': u'Farm Friends',
#         'animals': [
#             {
#                 'id': 3,
#                 'name': u'Louis',
#                 'events': [
#                     {
#                         'id': 5,
#                         'task': u'teeth cleaning',
#                         'due': u'5/1/17'
#                     },
#                     {
#                         'id': 6,
#                         'task': u'deworming',
#                         'due': u'4/23/17'
#                     }
#                 ]
#             },
#             {
#                 'id': 4,
#                 'name': u'Isaac',
#                 'events': [
#                     {
#                         'id': 7,
#                         'task': u'hoof maintenance',
#                         'due': u'1/15/17'
#                     },
#                     {
#                         'id': 8,
#                         'task': u'antibiotics',
#                         'due': u'4/15/17'
#                     }
#                 ]
#             }
#         ]
#     }
# ]

# NON-API ROUTES
@app.route('/sanctuary')
@app.route('/')
def index():
    return render_template('index.html')


# DATABASE
# SANCTUARY
class Sanctuary(db.Model):
    __tablename__ = "sanctuaries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    animals = db.relationship('Animal', backref='sanctuary')

    def json_dump(self):
        animals = []
        for animal in self.animals:
            # Add animal to the list
            animals.append(animal.json_dump())

        return {
            "id": self.id,
            "name": self.name,
            "animals": animals
        }

    def __repr__(self):
        return '<Sanctuary name %r>' % self.name

# ANIMAL
class Animal(db.Model):
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    sanctuary_id = db.Column(db.Integer, db.ForeignKey('sanctuaries.id'))
    events = db.relationship('Event', backref='animal')
    name = db.Column(db.String(120), unique=True)

    def json_dump(self):
        events = []
        for event in self.events:
            # Add animal to the list
            events.append(event.json_dump())

        return {
            "id": self.id,
            "name": self.name,
            "events": events
        }

    def __repr__(self):
        return '<Animal name %r>' % self.name

# EVENT
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    task = db.Column(db.String(120), unique=True)
    due = db.Column(db.String(120), unique=True)

    def json_dump(self):
        return dict(id=self.id, task=self.task, due=self.due)

    def __repr__(self):
        return '<Task %r>' % self.task

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
    call_sanctuaries = Sanctuary.query.all()

    return jsonify({'sanctuaries': [sanctuary.json_dump() for sanctuary in call_sanctuaries]})

@app.route('/sanctuary/api/sanctuaries/<int:id>', methods=['GET'])
def get_sanctuary(id):
    call_sanctuary = Sanctuary.query.get_or_404(id)
    # sanctuary = [sanctuary for sanctuary in sanctuaries if sanctuary['sanctuaryId'] == sanctuary_id]
    # if len(sanctuary) == 0:
    #     abort(404)
    return jsonify(sanctuaries = [call_sanctuary.json_dump()])

@app.route('/sanctuary/api/sanctuaries', methods=['POST'])
def create_sanctuary():
    if not request.json or not 'name' in request.json:
        abort(400)
    sanctuary = {
        'id': db[-1]['id'] + 1,
        'name': request.json['name'],
    }
    db.append(sanctuary)
    return jsonify({'sanctuary': sanctuary}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_sanctuary(sanctuary):
    new_sanctuary = {}
    for field in sanctuary:
        if field == 'id':
            new_sanctuary['uri'] = url_for('get_sanctuary', id=sanctuary['id'], _external=True)
        new_sanctuary[field] = sanctuary[field]
    return new_sanctuary


# ANIMALS
@app.route('/sanctuary/api/animals', methods=['GET'])
def get_animals():
    call_animals = Animal.query.all()

    return jsonify({'animals': [animal.json_dump() for animal in call_animals]})

@app.route('/sanctuary/api/animals/<int:id>', methods=['GET'])
def get_animal(id):
    call_animal = Animal.query.get_or_404(id)
    # animal = [animal for animal in animals if animal['id'] == animal_id]
    # if len(animal) == 0:
    #     abort(404)
    return jsonify(animals = [call_animal.json_dump()])

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

@app.route('/sanctuary/api/animals/<int:id>', methods=['DELETE'])
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
            new_animal['uri'] = url_for('get_animal', id=animal['id'], _external=True)
        new_animal[field] = animal[field]
    return new_animal

# EVENTS
# Add int:animal_id
@app.route('/sanctuary/api/events', methods=['GET'])
def get_events():
    call_events = Event.query.all()

    return jsonify({'events': [event.json_dump() for event in call_events]})

@app.route('/sanctuary/api/events/<int:id>', methods=['GET'])
def get_event(id):
    call_event = Event.query.get_or_404(id)
    # event = [event for event in events if event['id'] == event_id]
    # if len(event) == 0:
    #     abort(404)
    return jsonify(events = [call_event.json_dump()])

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

@app.route('/sanctuary/api/events/<int:id>', methods=['PUT'])
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

@app.route('/sanctuary/api/events/<int:id>', methods=['DELETE'])
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
