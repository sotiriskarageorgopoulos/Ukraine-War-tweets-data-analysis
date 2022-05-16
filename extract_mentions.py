import re
import pandas as pd

df = pd.read_csv('./clear_data/tweets.csv')

tweets_text = df["text"]
mentions = []
for tweet in tweets_text:
    tweet_mentions = re.findall("@([a-zA-Z0-9_]{1,50})", tweet)
    mentions.extend(tweet_mentions)
    
mentions_df = pd.DataFrame({"mentions": mentions})
mentions_df.to_csv('./clear_data/mentions.csv')