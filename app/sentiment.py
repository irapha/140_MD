import requests


API_KEY = '021c7fbb7087642804d04224864418c7'

def get_sentiment(tweet):
    request_url = 'http://api.datumbox.com/1.0/SentimentAnalysis.json'
    r = requests.post(request_url, data={ 'api_key': API_KEY, 'text': tweet })
    json = r.json()
    if json['output']['status'] == 0:
        print(json['output']['error'])
    return r.json()['output']['result']
