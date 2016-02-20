from app import app
from twitter import get_tweets


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/user/<username>')
def stats(username):
    # Call functions that compute stats for user
    print get_tweets(username)
    return username + ' statistics: you sleep too much. #sleepisfortheweak.'
