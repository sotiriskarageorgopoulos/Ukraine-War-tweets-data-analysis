import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./clear_data/tweets.csv",sep=",")
df_hashtags = pd.read_csv("./clear_data/hashtags.csv",sep=",")
df_mentions = pd.read_csv("./clear_data/mentions.csv",sep=",")

sensitive_content_count = df[df["possibly_sensitive"] == True]["possibly_sensitive"].count()
non_sensitive_content_count = df[df["possibly_sensitive"] == False]["possibly_sensitive"].count()

content_categories = ['sensitive content','no sensitive content']
content_count = [sensitive_content_count,non_sensitive_content_count]

count_of_sources = pd.DataFrame(df.groupby(["source"])["source"].count())
top_5_sources_count = list(count_of_sources.stack().nlargest(5))

langs_from_csv = dict(df.groupby('lang')['lang'].count())
lang_df = pd.DataFrame.from_dict({
    "language": list(langs_from_csv.keys()),
    "tweets": list(langs_from_csv.values()),
})

hashtags_count = dict(df_hashtags.groupby('hashtags')['hashtags'].count())
top_10_hashtags_count = list(sorted(hashtags_count.items(), key=lambda item: item[1],reverse=True))[:10]
top_10_hashtags_df = pd.DataFrame({
    "hashtag": map(lambda item: item[0],top_10_hashtags_count),
    "count": map(lambda item: item[1],top_10_hashtags_count)
})

mentions_count = dict(df_mentions.groupby('mentions')['mentions'].count())
top_10_mentions_count = list(sorted(mentions_count.items(),key=lambda item: item[1],reverse=True))[:10]
top_10_mentions_df = pd.DataFrame({
    "mention": map(lambda item: item[0],top_10_mentions_count),
    "count": map(lambda item: item[1],top_10_mentions_count)
})

sns.set_theme(style="whitegrid")
#top 10 hashtags plot
hashtags_plot = sns.barplot(data=top_10_hashtags_df,x="hashtag",y="count")
plt.show()

#top 20 mentions plot
mentions_plot = sns.barplot(data=top_10_mentions_df,x="mention",y="count")
plt.show()

#languages plot
lang_plot = sns.barplot(data=lang_df, x="language",y="tweets", palette="rocket")
plt.show(block=False)
plt.pause(3000)

#content barplot
content_plot = sns.barplot(x=content_categories, y=content_count, palette="deep")
content_plot.set_ylabel("tweets")
content_plot.set_xlabel("content categories")
plt.show(block=False)
plt.pause(3000)

#top 10 sources barplot
sources = ['Twitter for Android','Twitter Web App','Twitter for iPhone','Twitter for iPad','TweetDeck']
sources_barplot = sns.barplot(x=sources,y=top_5_sources_count,palette="deep")
sources_barplot.set_xlabel("sources")
sources_barplot.set_ylabel("tweets")
plt.show(block=False)
plt.pause(3000)


