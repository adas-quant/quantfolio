# Twitter/X Data Analysis for Trading Signals (Indian Markets)

This project converts Twitter/X chatter from Indian market hashtags (e.g., **#nifty50**, **#sensex**, **#banknifty**, **#intraday**) into quantitative signals for trading research.

---

## ✨ Features
- **No paid APIs** – works with `snscrape` / `twscrape` / web sources.
- **Clean processing** → stored in **Parquet** (fast, compressed, columnar).
- **Text-to-signal conversion** using TF-IDF + engagement metrics.
- **Composite trading signal** with a simple confidence score.
- **Memory-efficient visualization** using resampled time-series.

---

## 📂 Project Structure
```bash
twitter-data-analysis-for-trading-signals/
│── README.md
│── requirements.txt
│── .gitignore
│
├── src/
│   ├── process.py
│   ├── analyze.py
│   ├── scrapper.py
│   └── parquet_view.py
│
├── data/
│   ├── raw/
│   │   └── raw_tweets.json              # demo raw tweets
│   └── processed/
│       ├── processed_tweets.parquet     # demo processed output
│       └── processed_tweets.csv         # same data, CSV for easy viewing
│
├── artifacts/
│   └── market_signal_visualization.png  # sample visualization
│
└── logs/                                # runtime logs (ignored in git)
```

---

## ⚙️ Setup

> Recommended: **Python 3.10** (tested). Create and use a venv.

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1) Process raw tweets
```bash
python src/process.py data/raw/raw_tweets.json data/processed/processed_tweets.parquet
```

**(Optional) export to CSV for easier viewing:**
```bash
python -c "import pandas as pd; pd.read_parquet('data/processed/processed_tweets.parquet').to_csv('data/processed/processed_tweets.csv', index=False)"
```

### 2) Analyze & visualize
```bash
python src/analyze.py data/processed/processed_tweets.parquet
```

➡️ Output plot: `artifacts/market_signal_visualization.png`

---

## 📊 Output Columns

From `process.py`:
- `id`
- `timestamp_utc`
- `username`
- `user_followers`
- `user_location`
- `content`
- `cleaned_content`
- `hashtags`
- `mentioned_users`
- `like_count`
- `retweet_count`
- `reply_count`
- `quote_count`
- `url`

---

## 🧠 Methodology

- **TF-IDF (100 features)** on `cleaned_content` → `buzz_signal` (sum per tweet).  
- Normalize: `buzz_signal`, `retweet_count`, `like_count`.  
- **Composite signal** = `0.6*buzz + 0.3*retweets + 0.1*likes`.  
- **Confidence score** = scaled `user_followers`.  
- **Visualization** = resampled (15-minute) composite signal + confidence.  

---

## 📝 Notes

- Included data files are **small demo samples** to illustrate the pipeline.  
- For large-scale runs, keep only Parquet outputs in git and store full datasets elsewhere.  
- Compatible with extension to **FinBERT/VADER** for richer sentiment.  

---

## 📌 Recruiter Note

This repo demonstrates:
- End-to-end **data engineering + ML pipeline** from social media to signals.  
- Use of **efficient formats (Parquet)** and **vectorization (TF-IDF)**.  
- **Production-style practices**: modular scripts, `.gitignore`, README, requirements.  

---

## 📜 License

For educational / demo use only. Please verify compliance with Twitter/X data terms for any production usage.
