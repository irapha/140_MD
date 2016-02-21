import requests


API_KEY = '4ae65adf24d114a6325399d2b77b3722'

def get_sentiment(tweet):
    request_url = 'http://api.datumbox.com/1.0/SentimentAnalysis.json'
    r = requests.post(request_url, data={ 'api_key': API_KEY, 'text': tweet })
    return r.json()['output']['result']
