import pandas as pd
from numpy import mean,std,unique
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.model_selection import KFold,cross_val_score,cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer,f1_score,recall_score
import seaborn as sns
import matplotlib.pyplot as plt

tweets = pd.read_csv("./clear_data/tweets.csv")
en_mlma_df = pd.read_csv("./clear_data/en_dataset.csv")

print(en_mlma_df["target"].unique())

#Classifier statistical estimation for english data set
cv = KFold(n_splits=10, random_state=1, shuffle=True)

text_clf = Pipeline([('count_texts', CountVectorizer()),
                     ('tf_idf', TfidfTransformer()),
                     ('classifier', MultinomialNB()),
                    ])

predictions = cross_val_predict(text_clf, en_mlma_df["tweet"], en_mlma_df["target"], cv=cv)
accuracy_scores = cross_val_score(text_clf,en_mlma_df["tweet"], en_mlma_df["target"], scoring='accuracy', cv=cv, n_jobs=-1)
f1_scores = cross_val_score(text_clf,en_mlma_df["tweet"], en_mlma_df["target"], scoring=make_scorer(f1_score, average='weighted', labels=["offensive","normal"]), cv=cv, n_jobs=-1)
recall_scores = cross_val_score(text_clf,en_mlma_df["tweet"], en_mlma_df["target"], scoring=make_scorer(recall_score, average='weighted', labels=["offensive","normal"]), cv=cv, n_jobs=-1)

print(f'Mean Accuracy: {mean(accuracy_scores)} \n Std Accuracy: {std(accuracy_scores)}')
print(f'Mean F1 Score: {mean(f1_scores)} \n Std F1 Score: {std(f1_scores)}')
print(f'Mean Recall: {mean(recall_scores)} \n Std Recall Score: {std(recall_scores)}')

#Prediction of tweets label
text_clf = text_clf.fit(en_mlma_df["tweet"], en_mlma_df["target"])
tweets_in_en = tweets[tweets["lang"] == "en"]
en_predictions = text_clf.predict(tweets_in_en["text"])

u,count = unique(en_predictions,return_counts=True)
print(count)
print(u)


# fig, axs = plt.subplots(ncols=2)
# sns.pie()
