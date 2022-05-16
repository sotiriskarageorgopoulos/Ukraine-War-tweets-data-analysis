import pandas as pd
from pandas_profiling import ProfileReport
from pathlib import Path 
import logging  

logging.basicConfig(level = logging.INFO)
tweets_csv_file = Path('./clear_data/tweets.csv')  
df = pd.read_csv('./clear_data/tweets.csv')

def create_data_profile():
    profile = ProfileReport(df,minimal=True)
    profile.to_file("data_profile.html")
    
def clear_duplicate_values():
    df_records_before = len(df)
    df.drop_duplicates(keep=False,inplace=True)
    df.to_csv(tweets_csv_file)
    df_records_after = len(df)
    logging.info("The tweets.csv is cleared from duplicates records...")
    logging.info(f"{df_records_before - df_records_after} duplicate records is removed...")
    
create_data_profile()