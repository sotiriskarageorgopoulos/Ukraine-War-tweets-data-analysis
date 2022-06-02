import seaborn as sns    
import pandas as pd
import matplotlib.pyplot as plt

tweets = pd.read_csv("./clear_data/tweets.csv",sep=",")

tweets["created_at"] = tweets["created_at"].str.slice(start=0,stop=10)

sns.set(font_scale=1.1)
quote_reply_plot = sns.lmplot(x="quote_count",y="reply_count",col="created_at",data=tweets)
quote_reply_plot.set_axis_labels("quotes","replies")
plt.show(block=False)
plt.pause(3000)

sns.set(font_scale=1.1)
quote_like_plot = sns.lmplot(x="quote_count",y="like_count",col="created_at",data=tweets)
quote_like_plot.set_axis_labels("quotes","likes")
plt.show(block=False)
plt.pause(3000)

sns.set(font_scale=1.1)
reply_like_plot = sns.lmplot(x="reply_count",y="like_count",col="created_at",data=tweets)
reply_like_plot.set_axis_labels("replies","likes")
plt.show(block=False)
plt.pause(3000)