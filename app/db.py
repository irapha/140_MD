from firebase import firebase

firebase = firebase.FirebaseApplication("https://140md.firebaseio.com/", None)

def get_sleep():
    """Returns average number of hours of sleep."""
    return firebase.get('/hours_sleep', None)

def get_num_users():
    return firebase.get('/num_users', None)

def update_sleep(hours_sleep):
    avg_hours_sleep = get_sleep()
    num_users = get_num_users()

    new_hours_sleep = (hours_sleep + avg_hours_sleep * num_users) / (num_users + 1)

    firebase.put('/', 'num_users', num_users + 1)
    firebase.put('/', 'hours_sleep', new_hours_sleep)


def get_positive():
    return firebase.get('/positive', None)

def get_negative():
    return firebase.get('/negative', None)

def get_neutral():
    return firebase.get('/neutral', None)

def update_sentiment(pos, neg, neu):
    pos = pos + get_positive()
    neg = neg + get_negative()
    neu = neu + get_neutral()
    firebase.put('/', 'positive', pos)
    firebase.put('/', 'negative', neg)
    firebase.put('/', 'neutral', neu)
