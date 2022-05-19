import seaborn as sns 
import pandas as pd   
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt

tweets = pd.read_csv("./clear_data/tweets.csv",sep=",")
tweets["created_at"] = tweets["created_at"].str.slice(start=0,stop=13)

tweets_by_like_sum = dict(tweets.groupby(['created_at'])["like_count"].sum())
tweets_by_quote_sum = dict(tweets.groupby(['created_at'])["quote_count"].sum())
tweets_by_reply_sum = dict(tweets.groupby(['created_at'])["reply_count"].sum())
tweets_by_retweet_sum = dict(tweets.groupby(['created_at'])["retweet_count"].sum())
tweets_by_count = dict(tweets.groupby(['created_at'])["created_at"].count())

tweets_by_count_dict = {
    "date": list(tweets_by_count.keys()), 
    "tweets": list(tweets_by_count.values())
}

tweets_by_like_dict = {
    "date": list(tweets_by_like_sum.keys()),
    "likes": list(tweets_by_like_sum.values())
}

tweets_by_quote_dict = {
    "date": list(tweets_by_quote_sum.keys()),
    "quotes": list(tweets_by_quote_sum.values())
}

tweets_by_reply_dict = {
    "date": list(tweets_by_reply_sum.keys()),
    "replies": list(tweets_by_reply_sum.values())
}

tweets_by_retweet_dict = {
    "date": list(tweets_by_retweet_sum.keys()),
    "retweets": list(tweets_by_retweet_sum.values())
}

tweets_by_like_df = pd.DataFrame.from_dict(tweets_by_like_dict)
tweets_by_quote_df = pd.DataFrame.from_dict(tweets_by_quote_dict)
tweets_by_reply_df = pd.DataFrame.from_dict(tweets_by_reply_dict)
tweets_by_retweet_df = pd.DataFrame.from_dict(tweets_by_retweet_dict)
tweets_by_count_df = pd.DataFrame.from_dict(tweets_by_count_dict)


fig1, axs1 = plt.subplots(nrows=3,ncols=2)
fig2, axs2 = plt.subplots(nrows=2,ncols=2)

def create_timeseries_diag(y_col,df,axis):
    plot = sns.lineplot(x='date',y=y_col,data=df,ax=axis)
    plot.xaxis.set_ticklabels([])

autocorrelation_plot(tweets_by_like_df["likes"],axs1[0,1])
autocorrelation_plot(tweets_by_quote_df["quotes"],axs1[1,1])
autocorrelation_plot(tweets_by_reply_df["replies"],axs1[2,1])
create_timeseries_diag('likes',tweets_by_like_df,axs1[0,0])
create_timeseries_diag('quotes',tweets_by_quote_df,axs1[1,0])
create_timeseries_diag('replies',tweets_by_reply_df,axs1[2,0])

create_timeseries_diag('retweets',tweets_by_retweet_df,axs2[0,0])
create_timeseries_diag('tweets',tweets_by_count_df,axs2[1,0])
autocorrelation_plot(tweets_by_retweet_df["retweets"],axs2[0,1])
autocorrelation_plot(tweets_by_count_df["tweets"],axs2[1,1])
plt.show(block=False)
plt.pause(3000)