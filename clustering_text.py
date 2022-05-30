from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import warnings
import nltk
nltk.download('punkt')
warnings.filterwarnings("ignore")

def tokenize(string): 
    blob = TextBlob(string.lower())
    tokens = blob.words
    words = [token.stem() for token in tokens]
    return words

tweets = pd.read_csv("./clear_data/tweets.csv")
en_tweets = tweets[tweets["lang"] == "en"][:5000]

tf_idf_vector = TfidfVectorizer(tokenizer=tokenize,
                                stop_words='english',
                                norm="l1")
texts_tf_idf = tf_idf_vector.fit_transform(en_tweets["text"]).toarray()
# texts_df = pd.DataFrame(texts_tf_idf,columns=tf_idf_vector.get_feature_names())

pca = PCA(2)
principal_components = pca.fit_transform(texts_tf_idf)
kmeans_algo = KMeans(n_clusters=4, random_state=0)
labels = kmeans_algo.fit_predict(principal_components)
u_labels = np.unique(labels) 

s = silhouette_score(principal_components, labels, metric="euclidean")
print(f"Silhouette score is: {s}")

sns.scatterplot(x=principal_components[:,0], y=principal_components[:,1], hue=labels, palette="deep")
plt.show(block=False)
plt.pause(3000)