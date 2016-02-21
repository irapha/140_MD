from app import app
from app.twitter import get_tweets
from app.stats import get_statistics
from flask import render_template
from flask import request
from flask import redirect


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get("TwitterName")
        print(request.form)
        return redirect("/user/" + username, code=302)
    return render_template('index.html')



@app.route('/user/<username>')
def render_stats(username):
    tweets = get_tweets(username)
    stats = get_statistics(tweets)
    return render_template('layout.html', stats=stats)
