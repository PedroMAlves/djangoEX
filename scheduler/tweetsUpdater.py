import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import json
from pythonTips import models
from utility import converter


auth_params = {
    'app_key':'zF0YxZ9MKJEQgYqbr1VucLgJd',
    'app_secret':'2vZYyaJhp4dk5qil3WN6P3mL8LeLsfoHa20sFLSAVxT7cdbHQJ',
    'oauth_token':'1170455821194530816-xEeVkfgt7QYaJbAukDtfgCvDYTt6bO',
    'oauth_token_secret':'9pB197WDVndmGNzBeKoPa1g3wPNcczyOPoG8f6blv2Jwf'
}

auth = OAuth1 (
    auth_params['app_key'],
    auth_params['app_secret'],
    auth_params['oauth_token'],
    auth_params['oauth_token_secret']
)

url_rest = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'count': 100, 'lang': 'en', 'screen_name': 'python_tip'}

def update_db():
    results = requests.get(url_rest, params=params, auth=auth)
    tweets = results.json()
    for tweet in tweets:
        print(tweet["user"]["screen_name"])
        print(type(tweet["user"]["screen_name"]))
        if models.Tweets.objects.filter(twitter_id=tweet["id"]).count() == 0:
            date = tweet["created_at"].split(" ")
            formated_date = date[5] + "-" + converter.convert_str_to_month(date[1]) + "-" + date[2] + " " + date[3]
            models.Tweets(time_stamp=formated_date, python_tip=tweet["text"], twitter_id=tweet["id"]).save()
    
    #with open('test.txt', 'w') as f:
    #    f.write(json.dumps(tweets))
    print("working")