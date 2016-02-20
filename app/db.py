from firebase import firebase

firebase = firebase.FirebaseApplication("https://140md.firebaseio.com/", None)

def get_sleep():
    """Returns average number of hours of sleep."""
    return firebase.get('/hours_sleep', None)

def get_num_users():
    return firebase.get('/num_users', None)

def update(hours_sleep):
    avg_hours_sleep = get_sleep()
    num_users = get_num_users()

    new_hours_sleep = (hours_sleep + avg_hours_sleep * num_users) / (num_users + 1)

    firebase.put('/', 'num_users', num_users + 1)
    firebase.put('/', 'hours_sleep', new_hours_sleep)

