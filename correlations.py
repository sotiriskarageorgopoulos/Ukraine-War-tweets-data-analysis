import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./clear_data/tweets.csv",sep=",")
print(df.corr(method="pearson"))

sns.set_theme(style="darkgrid")
sns.jointplot(x=df["quote_count"],y=df["reply_count"],color="r",kind="reg")
sns.jointplot(x=df["quote_count"],y=df["like_count"],color="r",kind="reg")
sns.jointplot(x=df["reply_count"],y=df["like_count"],color="r",kind="reg")

plt.show(block=False)
plt.pause(3000)