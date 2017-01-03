from app import app

@app.route('/')
@app.route('/index')
def index():
    return "MVP, my ass. This is good enough!"
