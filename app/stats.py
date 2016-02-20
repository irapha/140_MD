from datetime import datetime

def count(tweets):
    if not tweets:
        return {}

    utc_offset = tweets[0]['user']['utc_offset'] / 3600

    counts = dict()
    for tweet in tweets:
        timestamp = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        minutes = (((timestamp.hour + utc_offset) % 24) * 60 + timestamp.minute)
        if minutes not in counts:
            counts[minutes] = 0
        counts[minutes] += 1
    return counts

def get_poisson_dists(tweets):
    counts = count(tweets)

    probs = dict()
    for timestep in range(0, 24*60, 5):
        probs[timestep] = 0
        for t in counts:
            if timestep - 60 <= t < timestep + 60 or \
               timestep - 60 <= t - 24*60 < timestep + 60 or \
               timestep - 60 <= t + 24*60 < timestep + 60:
                probs[timestep] += counts[t] / 60
    return probs

def get_statistics(tweets):
    probs = jsonify_dist(get_poisson_dists(tweets))
    stats = {
        'well_rested': True,
        'rest_percentage': 17,
        'probs': probs
        }
    return stats

def squareFit(tweets):
    probs = get_poisson_dists(tweets)
    maxVal = max(probs, probs.get) #find the max of the set
    mylist = [maxVal, 0, 0]
    for timestep in range(0, 24 * 60, 5)
        for distancestep in range (60, 24 * 60, 20)
            variance = varianceCalc(timestep, distancestep, probs, maxVal)
            if (variance < mylist.get(1))
                mylist[1] = variance
                mylist[2] = timestep
                mylist[3] = distancestep
    return mylist

def varianceCalc(timestep, distancestep, probs, maxVal):
    position1 = timestep
    varaince = 0
    base = 5
    for timestep in range(timestep, 24 * 60 + timestep, 5)
        if (timestep > postition1 and timestep < (position1 + distancestep))
            variance = variance + base * (probs[timestep%(24 * 60)] - maxVal)^2
        else
            variance = variance + base * (probs[timestep%(24 * 60)])^2
    return variance

def sleepCoefficient(mylist, maxVal):
    coefficient = mylist[1] / ((maxVal^2) * (60 * 24))

def jsonify_dist(probs):
    json = []
    for k in probs:
        json.append([k, probs[k]])
    return json
