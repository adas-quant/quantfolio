# analyze.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np

def analyze_data(input_parquet_path='processed_tweets.parquet'):
    """
    Loads processed data and performs analysis to generate trading signals.
    """
    print("Loading processed data for analysis...")
    df = pd.read_parquet(input_parquet_path)

    # Ensure data is sorted by time for time-series analysis
    df.sort_values('timestamp_utc', inplace=True)
    df.set_index('timestamp_utc', inplace=True)

    print("Data loaded. Starting analysis...")

    # --- 1. Text-to-Signal Conversion (TF-IDF) ---
    print("\n--- Generating TF-IDF based Buzz Signal ---")
    # Use a small number of features for a simple "buzz" score
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['cleaned_content'].dropna())

    # Create a simple "buzz" signal by summing the TF-IDF scores for each tweet
    # This represents the overall importance of the terms in that tweet.
    df['buzz_signal'] = np.asarray(tfidf_matrix.sum(axis=1)).ravel()
    print("Top 10 words by TF-IDF:", vectorizer.get_feature_names_out()[:10])


    # --- 2. Signal Aggregation ---
    print("\n--- Creating a Composite Trading Signal ---")
    # Combine multiple features into a single signal
    # We will use buzz_signal, retweet_count, and like_count
    
    # Normalize the features to be on a similar scale (0 to 1)
    scaler = MinMaxScaler()
    df[['buzz_normalized', 'retweets_normalized', 'likes_normalized']] = scaler.fit_transform(
        df[['buzz_signal', 'retweet_count', 'like_count']]
    )

    # Define weights for each component
    # Let's say content buzz is most important
    weights = {'buzz': 0.6, 'retweets': 0.3, 'likes': 0.1}

    # Calculate the composite signal
    df['composite_signal'] = (
        weights['buzz'] * df['buzz_normalized'] +
        weights['retweets'] * df['retweets_normalized'] +
        weights['likes'] * df['likes_normalized']
    )
    
    # Calculate a confidence interval (e.g., based on user followers)
    # Here, we create a simple confidence score: more followers = higher confidence
    df['confidence'] = scaler.fit_transform(df[['user_followers']])
    
    print("Sample of generated signals:")
    print(df[['composite_signal', 'confidence']].head())


    # --- 3. Memory-Efficient Visualization ---
    print("\n--- Generating Visualizations ---")
    # To visualize large datasets, we resample the data instead of plotting every point.
    # Let's resample the signals to a 15-minute interval.
    
    resampled_df = df['composite_signal'].resample('15T').mean().dropna()
    resampled_confidence = df['confidence'].resample('15T').mean().dropna()

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax1 = plt.subplots(figsize=(15, 7))

    # Plot the aggregated signal
    ax1.plot(resampled_df.index, resampled_df.values, label='Aggregated Composite Signal (15min avg)', color='b')
    ax1.set_xlabel('Time (UTC)')
    ax1.set_ylabel('Composite Signal Strength', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('Aggregated Market Buzz Signal Over Time')
    
    # Create a second y-axis for confidence
    ax2 = ax1.twinx()
    ax2.plot(resampled_confidence.index, resampled_confidence.values, label='Avg. Confidence (15min avg)', color='g', linestyle='--')
    ax2.set_ylabel('Average Confidence Score', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    fig.tight_layout()
    plt.legend()
    
    # Save the plot to a file
    plot_filename = 'market_signal_visualization.png'
    plt.savefig(plot_filename)
    print(f"Visualization saved to {plot_filename}")
    plt.show()


if __name__ == '__main__':
    analyze_data()
