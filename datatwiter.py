# import tweepy
import tweepy as tw
import pandas as pd
import os
import dataintegration as dm
from dotenv import load_dotenv
load_dotenv()
# your Twitter API key and API secret
gcpfilepath = os.getenv('GCP_CREDENTIALS')
print(gcpfilepath)
my_api_key = os.getenv('API_KEY')
my_api_secret = os.getenv('API_KEY_SECRET')
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "ikea -filter:retweets"
# get tweets from the API

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
    except:
        pass
    tweets_df = pd.concat([tweets_df,pd.DataFrame.from_records([{'user_name': tweet.user.name, 
                                               'user_location': tweet.user.location,\
                                               'user_description': tweet.user.description,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text, 
                                               'hashtags': ' '.join(str(e) for e in hashtags),
                                               'source': tweet.source}])])
    tweets_df = tweets_df.reset_index(drop=True)
# show the dataframe



dm.update_dable(tweets_df)