import re
import pandas as pd

df = pd.read_csv('./clear_data/tweets.csv')

tweets_text = df["text"]
hashtags = []
for tweet in tweets_text:
    tweet_hashtags= re.findall("#([a-zA-Z0-9_]{1,50})", tweet)
    hashtags.extend(tweet_hashtags)
    
hashtags_df = pd.DataFrame({"hashtags": hashtags})
hashtags_df.to_csv('./clear_data/hashtags.csv')