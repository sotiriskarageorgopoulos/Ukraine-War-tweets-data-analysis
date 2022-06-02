import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./clear_data/tweets.csv",sep=",")
sns.set(font_scale=2)
correlation_matrix = df[["retweet_count","reply_count","like_count","quote_count"]].corr(method="pearson")
sns.heatmap(correlation_matrix,annot=True,annot_kws={"size": 35})
plt.show()

sns.set_theme(style="darkgrid")
sns.set(font_scale=2)
sns.pairplot(df[["retweet_count","reply_count","like_count","quote_count"]], 
                    kind="reg",
                    plot_kws={
                        'line_kws':{'color':'#4d3735'},
                        'scatter_kws': {
                            'color': '#9c4f46'
                        }
                    },
                    diag_kws={'color':'#9c4f46'},
                    diag_kind="kde")
plt.show(block=False)
plt.pause(3000)