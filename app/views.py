from app import app
from app.twitter import get_tweets
from app.stats import get_poisson_dists


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/user/<username>')
def stats(username):
    # Call functions that compute stats for user
    tweets = get_tweets(username)
    probs = get_poisson_dists(tweets)

    print(probs)

    for t in sorted(probs):
        print(str(t) + ', ' + str(probs[t]))

    return username + ' statistics: you sleep too much. #sleepisfortheweak.'
