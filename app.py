from flask import Flask, render_template, jsonify, abort, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import psycopg2

from flask.ext.heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sanctuaries'
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

# API
# SANCTUARIES
@app.route('/sanctuary/api/sanctuaries', methods=['GET'])
def get_sanctuaries():
    call_sanctuaries = Sanctuary.query.order_by(Sanctuary.id).all()
    return jsonify({'sanctuaries': [sanctuary.json_dump() for sanctuary in call_sanctuaries]}), 200

@app.route('/sanctuary/api/sanctuaries/<int:sanc_id>', methods=['GET'])
def get_sanctuary(sanc_id):
    call_sanctuary = Sanctuary.query.get_or_404(sanc_id)
    return jsonify({"sanctuaries": [call_sanctuary.json_dump()]}), 200

@app.route('/sanctuary/api/sanctuaries', methods=['POST'])
def create_sanctuary():
    if not request.form or 'name' not in request.form:
        abort(400)
    s = Sanctuary()
    s.name = request.form["name"]  # Probably want a unique constraint on `name` in the database
    db.session.add(s)
    db.session.commit()

    response = jsonify({'sanctuaries': [s.json_dump()]})
    response.status_code = 201
    response.headers["Location"] = url_for("get_sanctuary", sanc_id=s.id)
    return response

@app.route('/sanctuary/api/sanctuaries/<int:sanc_id>', methods=['DELETE'])
def delete_sanctuary(sanc_id):
    call_sanctuary = Sanctuary.query.get_or_404(sanc_id)
    db.session.delete(call_sanctuary)
    db.session.commit()
    return "", 204

@app.route('/sanctuary/api/sanctuaries/<int:sanc_id>', methods=['PUT', 'PATCH'])
def update_sanctuary(sanc_id):
    sanctuary = Sanctuary.query.get_or_404(sanc_id)
    if "name" in request.values:
        sanctuary.name = request.values["name"]
    if "animals" in request.values:
        raise NotImplementedError()
    return "", 204

# ANIMALS
@app.route('/sanctuary/api/animals', methods=['GET'])
def get_animals():
    all_animals = Animal.query.order_by(Animal.id).all()
    rv = jsonify({'animals': [the_animal.json_dump() for the_animal in all_animals]})
    return rv

@app.route('/sanctuary/api/animals/sanctuary/<int:sanctuary_id>', methods=['GET'])
def get_animals_for_sanctuary(sanctuary_id):
    all_animals = Animal.query.filter_by(sanctuary_id=sanctuary_id).order_by(Animal.id).all()
    rv = jsonify({'animals': [the_animal.json_dump() for the_animal in all_animals]})
    return rv

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    call_animal = Animal.query.get_or_404(animal_id)
    return jsonify({'animals': [call_animal.json_dump()]}), 200

@app.route('/sanctuary/api/animals', methods=['POST'])
def create_animal():
    the_name = request.form['name']
    new_animal = Animal()
    new_animal.name = the_name
    if "sanctuary_id" in request.form:
        sanc_id = int(request.form["sanctuary_id"])
        s = Sanctuary.query.get_or_404(sanc_id)
        new_animal.sanctuary = s

    db.session.add(new_animal)
    try:
        db.session.commit()
    except psycopg2.IntegrityError:
        # This means user tried to add another animal with the same name as an extant animal
        abort(409)  # 409 => Conflict

    response = jsonify({'animals': [new_animal.json_dump()]})
    response.status_code = 201
    response.headers["Location"] = url_for("get_animal", animal_id=new_animal.id)
    return response

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    the_animal = Animal.query.get_or_404(animal_id)
    db.session.delete(the_animal)
    db.session.commit()
    return "", 204

@app.route('/sanctuary/api/animals/<int:animal_id>', methods=['PUT', 'PATCH'])
def update_animal(animal_id):
    the_animal = Animal.query.get_or_404(animal_id)

    if "name" in request.values:
        the_animal.name = str(request.values["name"])

    if "sanctuary_id" in request.values:
        the_animal.sanctuary = Sanctuary.query.get_or_404(int(request.values["sanctuary_id"]))

    if "events" in request.values:
        raise NotImplementedError()

    return "", 204

def make_public_animal(animal):
    new_animal = {}
    for field in animal:
        if field == 'id':
            new_animal['uri'] = url_for('get_animal', id=animal.id, _external=True)
        new_animal[field] = animal[field]
    return new_animal

# EVENTS
@app.route('/sanctuary/api/events', methods=['GET'])
def get_events():
    call_events = Event.query.order_by(Event.id).all()
    return jsonify({'events': [event.json_dump() for event in call_events]})

@app.route('/sanctuary/api/events/animal/<int:animal_id>', methods=['GET'])
def get_events_for_animal(animal_id):
    call_events = Event.query.filter_by(animal_id=animal_id).order_by(Event.id).all()
    return jsonify({'events': [event.json_dump() for event in call_events]})

@app.route('/sanctuary/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    call_event = Event.query.get_or_404(event_id)
    return jsonify({'events': [call_event.json_dump()]})

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
    return "", 204

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
