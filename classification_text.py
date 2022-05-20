import pandas as pd  

en_mlma_df = pd.read_csv("./clear_data/en_dataset.csv")
en_mlma_df_fullstop = pd.read_csv("./clear_data/en_dataset_with_stop_words.csv")
fr_mlma_df = pd.read_csv("./clear_data/fr_dataset.csv") 

print(fr_mlma_df["sentiment"].head())
print(en_mlma_df["sentiment"].unique())
print(en_mlma_df_fullstop["sentiment"].unique())