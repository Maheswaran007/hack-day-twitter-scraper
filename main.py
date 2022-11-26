# import tweepy
import tweepy as tw
import pandas as pd
import os
import datetime
from data_integration import update_table
from dotenv import load_dotenv
from access_secrets import access_secret
load_dotenv()
# your Twitter API key and API secret


secrets = access_secret()

my_api_key = secrets.get('API_KEY', '')
my_api_secret = secrets.get('API_KEY_SECRET', '')
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "ikea -filter:retweets"
# get tweets from the API

def twitter_scrapper(request):
    tweets = tw.Cursor(api.search_tweets,
                q=search_query,
                lang="en").items(100)

    # store the API responses in a list
    tweets_copy = []
    for tweet in tweets:
        tweets_copy.append(tweet)
        
    print("Total Tweets fetched:", len(tweets_copy))
    tweets_df = pd.DataFrame()
    # populate the dataframe
    for tweet in tweets_copy:
        hashtags = []
        try:
            for hashtag in tweet.entities["hashtags"]:
                hashtags.append(hashtag["text"])
            text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
        except Exception as ex:
            raise ex
        tweets_df = pd.concat([tweets_df,pd.DataFrame.from_records([{'user_name': tweet.user.name, 
                                                'user_location': tweet.user.location,\
                                                'user_description': tweet.user.description,
                                                'user_verified': tweet.user.verified,
                                                'created_ssdate': tweet.created_at,
                                                'text': text, 
                                                'hashtags': ' '.join(str(e) for e in hashtags),
                                                'source': tweet.source,
                                                'insertion_date': datetime.datetime.now()}])])
        tweets_df = tweets_df.reset_index(drop=True)



    update_table(tweets_df)
    return "success"