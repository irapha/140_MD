from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/user/<username>')
def stats(username):
    # Call functions that compute stats for user
    return username + ' statistics: you sleep too much. #sleepisfortheweak.'
