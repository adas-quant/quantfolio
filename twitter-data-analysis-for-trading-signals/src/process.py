# process.py
import pandas as pd
import re

def clean_tweet_content(text):
    """
    Cleans the tweet content by removing URLs, mentions, hashtags, and special characters.
    """
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r'\@\w+|\#','', text) # Remove mentions and hashtags
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation and special characters
    text = text.strip() # Remove leading/trailing whitespace
    return text.lower() # Convert to lowercase

def process_data(input_json_path='raw_tweets.json', output_parquet_path='processed_tweets.parquet'):
    """
    Loads raw data, processes it, and saves it to Parquet format.
    """
    print("Loading raw data...")
    # Load data from JSON into a pandas DataFrame
    df = pd.read_json(input_json_path)

    print("Processing data...")
    # --- Data Cleaning and Normalization ---

    # 1. Handle potential duplicates based on tweet ID
    df.drop_duplicates(subset=['id'], inplace=True)

    # 2. Convert timestamp to datetime object for time-based analysis
    df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])

    # 3. Clean the tweet content for NLP tasks
    df['cleaned_content'] = df['content'].apply(clean_tweet_content)

    # 4. Ensure numeric types for engagement metrics
    numeric_cols = ['like_count', 'retweet_count', 'reply_count', 'quote_count', 'user_followers']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Reorder columns for clarity
    final_columns = [
        'id', 'timestamp_utc', 'username', 'user_followers', 'user_location',
        'content', 'cleaned_content', 'hashtags', 'mentioned_users', 'like_count',
        'retweet_count', 'reply_count', 'quote_count', 'url'
    ]
    df = df[final_columns]

    print(f"Data processed. Shape of the DataFrame: {df.shape}")

    # --- Storage ---
    # Save the cleaned DataFrame to Parquet format
    # Parquet is highly efficient for analytics
    print(f"Saving processed data to {output_parquet_path}...")
    df.to_parquet(output_parquet_path, index=False)
    print("Done.")


if __name__ == '__main__':
    process_data()
