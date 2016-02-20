from client import Client


CONSUMER_KEY = ''
CONSUMER_SECRET = ''


def get_tweets(username, max_num=1000):
    client = Client(CONSUMER_KEY, CONSUMER_SECRET)
    request_url = 'https://api.twitter.com/1.1/statuses/home_timeline.json' +
        '?screen_name=' + str(username) +
        '&count=' + str(max_num)
    return client.request(request_url)

