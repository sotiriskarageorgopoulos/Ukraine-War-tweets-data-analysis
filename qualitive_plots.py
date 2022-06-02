import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("./clear_data/tweets.csv",sep=",")
df_hashtags = pd.read_csv("./clear_data/hashtags.csv",sep=",")
df_mentions = pd.read_csv("./clear_data/mentions.csv",sep=",")

sensitive_content_count = df[df["possibly_sensitive"] == True]["possibly_sensitive"].count()
non_sensitive_content_count = df[df["possibly_sensitive"] == False]["possibly_sensitive"].count()

content_categories = ['sensitive content','no sensitive content']
content_count = [sensitive_content_count,non_sensitive_content_count]

count_of_sources = pd.DataFrame(df.groupby(["source"])["source"].count())
top_5_sources_count = list(count_of_sources.stack().nlargest(5))

hashtags_count = dict(df_hashtags.groupby('hashtags')['hashtags'].count())
top_5_hashtags_count = list(sorted(hashtags_count.items(), key=lambda item: item[1],reverse=True))[:5]
top_5_hashtags_df = pd.DataFrame({
    "hashtag": map(lambda item: item[0],top_5_hashtags_count),
    "count": map(lambda item: item[1],top_5_hashtags_count)
})

mentions_count = dict(df_mentions.groupby('mentions')['mentions'].count())
top_5_mentions_count = list(sorted(mentions_count.items(),key=lambda item: item[1],reverse=True))[:5]
top_5_mentions_df = pd.DataFrame({
    "mention": map(lambda item: item[0],top_5_mentions_count),
    "count": map(lambda item: item[1],top_5_mentions_count)
})

langs_count = dict(df.groupby('lang')['lang'].count())
top_5_langs_count = list(sorted(langs_count.items(),key=lambda item: item[1],reverse=True))[:5]
langs_df = pd.DataFrame({
    "lang": langs_count.keys(),
    "count": langs_count.values()
})
top_5_langs_df = pd.DataFrame({
    "lang": map(lambda item: item[0],top_5_langs_count),
    "count": map(lambda item: item[1],top_5_langs_count)
})

hashtags_in_string = " ".join(h for h in df_hashtags["hashtags"])
mentions_in_string = " ".join(m for m in df_mentions["mentions"])
langs_in_string = " ".join(l for l in langs_df["lang"])
h_word_cloud = WordCloud(collocations = False, background_color = 'white').generate(hashtags_in_string)
m_word_cloud = WordCloud(collocations = False, background_color = 'white').generate(mentions_in_string)
l_word_cloud = WordCloud(collocations = False, background_color = 'white').generate(langs_in_string)

sns.set_theme(style="whitegrid")
sns.set(font_scale=2)
h_fig, h_axs = plt.subplots(nrows=2)
hashtags_plot = sns.barplot(data=top_5_hashtags_df,x="hashtag",y="count",ax=h_axs[0]) #top 10 hashtags bar plot

h_axs[1].imshow(h_word_cloud,interpolation='bilinear')
h_axs[1].axis("off")
plt.show(block=False)
plt.pause(3000)

m_fig, m_axs = plt.subplots(nrows=2)
mentions_plot = sns.barplot(data=top_5_mentions_df,x="mention",y="count",ax=m_axs[0]) #top 10 mentions bar plot

m_axs[1].imshow(m_word_cloud,interpolation='bilinear')
m_axs[1].axis("off")
plt.show(block=False)
plt.pause(3000)

#languages word cloud
l_fig, l_axs = plt.subplots(nrows=2)
sns.barplot(data=top_5_langs_df,x="lang",y="count",ax=l_axs[0])
l_axs[1].imshow(l_word_cloud,interpolation='bilinear')
plt.axis("off")
plt.show(block=False)
plt.pause(3000)

#content barplot
content_plot = sns.barplot(x=content_categories, y=content_count, palette="deep")
content_plot.set_ylabel("tweets")
content_plot.set_xlabel("content categories")
plt.show(block=False)
plt.pause(3000)

#top 5 sources barplot
sources = ['Twitter for Android','Twitter Web App','Twitter for iPhone','Twitter for iPad','TweetDeck']
sources_barplot = sns.barplot(x=sources,y=top_5_sources_count,palette="deep")
sources_barplot.set_xlabel("sources")
sources_barplot.set_ylabel("tweets")
plt.show(block=False)
plt.pause(3000)


