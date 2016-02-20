from app.client import Client


CONSUMER_KEY = 'cC5zlxowoKxqaBmLzupkCvRqc'
CONSUMER_SECRET = 'Qd9uT03YEY2vmTG1xW97PjTaoaABw90CQOhSeyfdSrEDlPdsZm'


def get_tweets(username, max_num=1000):
    client = Client(CONSUMER_KEY, CONSUMER_SECRET)
    request_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json' + \
        '?screen_name=' + str(username) + \
        '&count=' + str(max_num)
    tweets = client.request(request_url) # 200 tweets
    while len(tweets) < max_num:
        tweets.extend(client.request(request_url + '&max_id=' + str(tweets[-1]['id'])))
    return tweets
