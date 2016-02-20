from app import app
from twitter import get_tweets
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/user/<username>')
def stats(username):
    # Call functions that compute stats for user
    tweets = get_tweets(username)
    print(tweets[0])
    print(len(tweets))
    dists = dict()
    for tweet in tweets:
        timestamp = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        minutes = (timestamp.hour * 60 + timestamp.minute)
        if minutes not in dists:
            dists[minutes] = 0
        dists[minutes] += 1

    probs = dict()
    for timestep in xrange(0, 24*60, 5):
        probs[timestep] = 0
        for d in dists:
            if timestep - 60 <= d < timestep + 60 or \
               timestep - 60 <= d - 24*60 < timestep + 60 or \
               timestep - 60 <= d + 24*60 < timestep + 60:
                probs[timestep] += dists[d]

    print(probs)

    for t in sorted(probs):
        print(str(t) + ', ' + str(probs[t]))

    return username + ' statistics: you sleep too much. #sleepisfortheweak.'
