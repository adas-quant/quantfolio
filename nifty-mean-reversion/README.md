# 📘 Quant Strategy: Mean Reversion vs Trend Following (Nifty, 2015–Present)

This project explores and backtests various **mean reversion** and **trend-following** strategies on the Indian Nifty index using daily historical data from **2015 onward**.

We systematically tested multiple technical trading strategies to investigate:

> ❓ *Can mean reversion strategies beat Buy & Hold in a market like India that trends heavily upward?*

---

## 🔧 Data Source

- Nifty 50 Daily OHLC data (2015–Present)
- Source: Yahoo Finance (via `yfinance`)
- File used: `data/nifty_daily_data.csv`

---

## 🎯 Objective
To test the **effectiveness of mean reversion strategies** in the Indian market and explore alternatives that may outperform the traditional Buy & Hold approach.

---

---

## 📚 Table of Contents

- [Data Source](#-data-source)
- [Objective](#-objective)
- [Strategies Tested](#-strategies-tested)
- [Key Insights](#-key-insights)
- [Conclusion](#-conclusion)


## 🧪 Strategies Tested

### 🔹 1. Bollinger Bands Mean Reversion (`bollinger_band_backtest.py`)
- **Idea**: Buy when price dips below lower Bollinger Band and revert to mean.
- **Outcome**: ❌ **Failed**. Consistently underperformed. Rare trades, and those rarely worked.
- 📈 `plots/bollinger_vs_buyhold.png`

---

### 🔹 2. RSI Mean Reversion (`rsi_mean_reversion_backtest.py`)
- **Idea**: Buy when RSI < 30 (oversold), exit after 10 days.
- **Outcome**: ❌ **Underperformed** Buy & Hold. Often bought in downtrends.
- 📈 `plots/rsi_meanreversion_vs_buyhold.png`

---

### 🔹 3. RSI Momentum (`rsi_momentum_backtest.py`)
- **Idea**: Buy when RSI > 60, hold for 10 days.
- **Outcome**: ✅ **Better than mean reversion**, but still underperformed **Buy & Hold**.
- 📈 `plots/rsi_momentum_vs_buyhold.png`

---

### 🔹 4. SMA Mean Reversion – Long Only (`sma_meanreversion_longonly_backtest.py`)
- **Idea**: Buy when SMA20 < SMA50 (dip), hold for 10 days.
- **Outcome**: ❌ Performed poorly. Missed most rallies.
- 📈 `plots/sma_meanreversion_vs_buyhold.png`
- 📁 `results/sma_meanreversion_trades.csv`

---

### 🔹 5. SMA Mean Reversion – Always-in Market (`sma_meanreversion_alwaysin_backtest.py`)
- **Idea**: Stay always in market. Long if SMA20 > SMA50, Short otherwise.
- **Outcome**: ❌❌ Total failure. Massive drawdowns. Lost in both up and downtrends.
- 📈 `plots/sma_meanreversion_alwaysin_vs_buyhold.png`
- 📁 `results/sma_meanreversion_alwaysin_trades.csv`

---

### 🔹 6. SMA Trend Following – Long/Short (`sma_trendfollowing_long_short_backtest.py`)
- **Idea**: Stay Long when SMA20 > SMA50, Short when SMA20 < SMA50. Switch on crossover.
- **Outcome**: ✅ ✅ **Beat Buy & Hold!** Effectively captured trends.
- 📈 `plots/sma_trendfollowing_vs_buyhold.png`
- 📁 `results/sma_trendfollowing_trades.csv`

---

## 📌 Key Insights

- 📉 **Mean Reversion fails** in Indian equity markets that trend strongly.
- ❌ Bollinger and RSI dips are often traps in strong downtrends.
- ⚖️ **RSI Momentum** is better but still can’t outperform Buy & Hold.
- 📉 Always-in Mean Reversion strategy caused **major drawdowns**.
- ✅ **Trend-following SMA crossover strategy beat Buy & Hold** convincingly by capturing both uptrends and downtrends.
- 📊 Allowing **short positions** and **removing fixed holding periods** significantly improved performance.
- 🔄 Strategies that constantly adapt to market structure (like crossovers) outperform rigid mean-reversion rules.

---

## 🔍 Conclusion
This backtest series shows that **classic mean reversion strategies** do **not work reliably** in trending markets like India. On the other hand, **simple trend-following rules** such as SMA crossovers can generate **significant alpha**, especially when allowing both **long and short positions**.

Next steps will include:
- Adding **stop loss logic** to each strategy.
- Testing combinations (e.g., RSI + SMA filters).
- Applying to **other indices** (e.g., Bank Nifty, Midcap).
- Exploring **volatility filters** or dynamic position sizing.

Stay tuned. 📈
