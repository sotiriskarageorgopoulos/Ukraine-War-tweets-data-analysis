from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_tweets = pd.read_csv('./clear_data/tweets.csv')

texts = list(df_tweets["text"])
neutral_tweets = 0
pos_tweets = 0
neg_tweets = 0
sentiments = []

for t in texts:
    polarity = TextBlob(t).sentiment.polarity
    
    if polarity == 0:
       neutral_tweets += 1
       sentiments.append("neutral")
    elif 0 < polarity <= 1:
       pos_tweets += 1
       sentiments.append("positive")
    elif -1 <= polarity < 0:
       neg_tweets += 1
       sentiments.append("negative")

df_tweets["sentiments"] = sentiments
sentiments_df = pd.DataFrame.from_dict({
    "sentiments": ["positive","negative","neutral"],
    "tweets": [pos_tweets,neg_tweets,neutral_tweets]
})

print(sentiments_df)
sns.set(font_scale=1.5)
fig, axs = plt.subplots(ncols=3)
like_replies_plot = sns.scatterplot(data=df_tweets, x="like_count", y="reply_count", hue="sentiments", style="sentiments",ax=axs[2])
like_replies_plot.set_xlabel("likes")
like_replies_plot.set_ylabel("replies")

quote_replies_plot = sns.scatterplot(data=df_tweets, x="quote_count", y="reply_count", hue="sentiments", style="sentiments",ax=axs[1])
quote_replies_plot.set_xlabel("quotes")
quote_replies_plot.set_ylabel("replies")

sns.barplot(data=sentiments_df,x="sentiments",y="tweets",ax=axs[0])
plt.show()
plt.pause(3000)

