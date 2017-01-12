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
                        'task': 'teeth cleaning',
                        'due': '1/1/17'
                    },
                    {
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
                        'task': 'teeth floating',
                        'due': '1/15/17'
                    },
                    {
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
                'animalId': 3,
                'name': u'Louis',
                'events': [
                    {
                        'task': u'teeth cleaning',
                        'due': u'5/1/17'
                    },
                    {
                        'task': u'deworming',
                        'due': u'4/23/17'
                    }
                ]
            },
            {
                'animalId': 4,
                'name': u'Isaac',
                'events': [
                    {
                        'task': u'hoof maintenance',
                        'due': u'1/15/17'
                    },
                    {
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
  return render_template('index.html')

# API

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# @app.route('/sanctuary/api/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#     task[0]['title'] = request.json.get('title', task[0]['title'])
#     task[0]['description'] = request.json.get('description', task[0]['description'])
#     task[0]['done'] = request.json.get('done', task[0]['done'])
#     return jsonify({'task': task[0]})
#
# @app.route('/sanctuary/api/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     tasks.remove(task[0])
#     return jsonify({'result': True})
#
# def make_public_task(task):
#     new_task = {}
#     for field in task:
#         if field == 'id':
#             new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
#         else:
#             new_task[field] = task[field]
#     return new_task


# SANCTUARIES

@app.route('/sanctuary/api/sanctuaries', methods=['GET'])
def get_sanctuaries():
    return jsonify({'sanctuaries': sanctuaries})

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


# ANIMALS


# EVENTS

if __name__ == '__main__':
  app.run(debug=True)
