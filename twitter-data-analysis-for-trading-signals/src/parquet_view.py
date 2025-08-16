import pandas as pd

df = pd.read_parquet("processed_tweets.parquet")

print(df.head())         # first 5 rows
print(df.columns)        # all available columns
print(len(df))           # number of tweets in file

df.to_csv("processed_tweets.csv", index=False)
