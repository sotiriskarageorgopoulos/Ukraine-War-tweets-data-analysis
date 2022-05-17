import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./clear_data/tweets.csv",sep=",")

sensitive_content_count = df[df["possibly_sensitive"] == True]["possibly_sensitive"].count()
non_sensitive_content_count = df[df["possibly_sensitive"] == False]["possibly_sensitive"].count()

content_categories = ['sensitive content','no sensitive content']
content_count = [sensitive_content_count,non_sensitive_content_count]

content_df = pd.DataFrame()
count_of_sources = pd.DataFrame(df.groupby(["source"])["source"].count())
top_5_sources_count = list(count_of_sources.stack().nlargest(5))

#content barplot
sns.set_theme(style="whitegrid")
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


