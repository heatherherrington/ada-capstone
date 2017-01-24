from flask import Flask, redirect, render_template, session, jsonify, abort, make_response, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sanctuaries'
heroku = Heroku(app)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


# NON-API ROUTES
@app.route('/animal/<int:animal_id>')
@app.route('/sanctuary')
@app.route('/')
def index(animal_id=None):
    return render_template('index.html')


# DATABASE
# SANCTUARY
class Sanctuary(db.Model):
    __tablename__ = "sanctuaries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    animals = db.relationship('Animal', backref='sanctuary')

    def json_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "animals": [a.json_dump() for a in self.animals]
        }

    def __str__(self):
        rv = super(Sanctuary, self).__str__()
        info = " id=%s name=%r num_animals=%d" % (self.id, self.name, len(self.animals))
        rv = rv[:-1] + info + rv[-1]
        return rv

        # def __repr__(self):
        #     return '<Sanctuary name %r>' % self.name

# ANIMAL
class Animal(db.Model):
    __tablename__ = "animals"
    id = db.Column(db.Integer, primary_key=True)
    sanctuary_id = db.Column(db.Integer, db.ForeignKey('sanctuaries.id'))
    events = db.relationship('Event', backref='animal')
    name = db.Column(db.String(120), unique=True)

    # Constructor function needed to initialize animal - will also need for events
    def __init__(self, name=None):
        if name is not None:
            self.name = name

    def json_dump(self):
        events = []
        for event in self.events:
            # Add event to the list
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
    task = db.Column(db.String(120), unique=False)
    due = db.Column(db.String(120), unique=False)

    def __init__(self, task=None, due=None, animal_id=None):
        if task is not None:
            self.task = task
        if due is not None:
            self.due = due
        if animal_id is not None:
            self.animal_id = animal_id

    def json_dump(self):
        return dict(id=self.id, task=self.task, due=self.due, animal_id=self.animal_id)

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
    # print("HI")
    # print(request.method)
    # print(request.method == 'POST')
    name = None
    if request.method == 'POST':
        # print(request.form)
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
        animal_id = request.form['animal_id']
        reg = Event(task, due, animal_id)
        db.session.add(reg)
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
    if request.method == 'DELETE':
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
    return jsonify(animals = [call_animal.json_dump()])

@app.route('/sanctuary/api/animals', methods=['POST'])
def create_animal():
    if not request.json or not 'name' in request.json:
        abort(400)
    animal = {
        # 'id': animals[-1]['id'] + 1,
        'name': request.json['name'],
    }
    animals.append(animal)
    return jsonify({'animal': animal}), 201

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    the_animal = Animal.query.get_or_404(animal_id)
    db.session.delete(the_animal)
    db.session.commit()
    return "", 204

def make_public_animal(animal):
    new_animal = {}
    for field in animal:
        if field == 'id':
            new_animal['uri'] = url_for('get_animal', id=animal['id'], _external=True)
        new_animal[field] = animal[field]
    return new_animal

# EVENTS
@app.route('/sanctuary/api/events', methods=['GET'])
def get_events():
    call_events = Event.query.all()
    return jsonify({'events': [event.json_dump() for event in call_events]})

@app.route('/sanctuary/api/events/animal/<int:animal_id>', methods=['GET'])
def get_events_for_animal(animal_id):
    call_events = Event.query.filter_by(animal_id=animal_id).order_by(Event.id).all()
    return jsonify({'events': [event.json_dump() for event in call_events]})

@app.route('/sanctuary/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    if "animal_id" in request.values:
         a = Animal.query.get_or_404(int(request.values["animal_id"]))
         event.animal = a
    return "", 204
    # call_event = Event.query.get_or_404(event_id)
    # return jsonify({'events': [call_event.json_dump()]})

@app.route('/sanctuary/api/events', methods=['POST'])
def create_event():
    if not request.form or 'task' not in request.form or 'animal_id' not in request.form:
        abort(400)
    a_id = int(request.form["animal_id"])
    a = Animal.query.get_or_404(a_id)

    event = Event()
    event.task = str(request.form["task"])
    event.animal = a

    if "due" in request.form:
        event.due = str(request.form["due"])

    db.session.add(event)
    db.session.commit()

    response = jsonify({'events': [event.json_dump()]})
    response.status_code = 201
    response.headers["Location"] = url_for("get_event", event_id=event.id)
    return response

@app.route('/sanctuary/api/events/<int:event_id>', methods=['PUT', 'PATCH'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)

    if "task" in request.values:
        event.task = str(request.values["task"])
    if "due" in request.values:
        event.due = str(request.values["due"])
    if "animal_id" in request.values:
        a = Animal.query.get_or_404(int(request.values["animal_id"]))
        event.animal = a

@app.route('/sanctuary/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
     the_event = Event.query.get_or_404(event_id)
     db.session.delete(the_event)
     db.session.commit()
     return "", 204

def make_public_event(event):
    new_event = {}
    for field in event:
        if field == 'id':
            new_event['uri'] = url_for('get_event', event_id=event['id'], _external=True)
        new_event[field] = event[field]
    return new_event

if __name__ == '__main__':
  app.run(debug=True)
