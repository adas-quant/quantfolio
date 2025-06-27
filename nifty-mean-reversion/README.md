# 🔄 Nifty Mean Reversion Strategy

This project implements a simple **mean reversion strategy** using Bollinger Bands on Nifty 50 daily OHLC data.

---

## Strategy Logic

- **Instrument:** Nifty 50 (spot index)
- **Data Source:** NSE (via `nsepy`)
- **Indicators Used:** Bollinger Bands (20 SMA, ±2 std dev)
- **Entry Rule:** Buy when Close < Lower Band  
- **Exit Rule:** Sell when Close ≥ Middle Band  
- **Backtest Period:** Custom (2018–2024)

---

## Folder Structure

- `data/`: Contains downloaded Nifty OHLC CSV files  
- `strategy/`: Python code for backtest logic  
- `plots/`: Output plots showing PnL, drawdown, etc.

---

## Status

✅ Real data from NSE  
✅ Working backtest logic  
📊 PnL visualizations to be added
