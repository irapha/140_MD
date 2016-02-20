from app import app
from app.twitter import get_tweets
from app.stats import get_statistics
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/user/<username>')
def render_stats(username):
    tweets = get_tweets(username)
    stats = get_statistics(tweets)
    return render_template('layout.html', stats=stats)
