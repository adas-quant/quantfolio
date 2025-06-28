# 📊 Quantfolio: A Portfolio of Quantitative Trading Strategies

![GitHub last commit](https://img.shields.io/github/last-commit/adas-quant/quantfolio)
![GitHub repo size](https://img.shields.io/github/repo-size/adas-quant/quantfolio)
![GitHub license](https://img.shields.io/github/license/adas-quant/quantfolio)

Welcome to **Quantfolio** — a curated collection of algorithmic and quantitative trading strategies developed using Python, with real-market backtests and visual performance analytics.

This project is aimed at demonstrating hands-on skills in building, analyzing, and deploying strategies across various asset classes.


## 🗂 Table of Contents

- [Strategies](#-strategies)
- [Features](#-features)
- [Requirements](#-requirements)
- [Author](#-author)
- [Note](#-note)

---

## 🧪 Strategies

Each strategy has its own standalone GitHub repository. This portfolio acts as the central directory pointing to all those strategy repos.

| Strategy | Description | Asset Class | Link |
|----------|-------------|-------------|------|
| 🧪 Nifty Intraday Strangle | Sell CE + PE at ₹20 premium, with SL & EOD exit | Derivatives (India) | [nifty-options-strategy-backtest](./nifty-options-strategy-backtest) |
| 📆 Nifty Positional Strangle *(In Progress)* | Delta-neutral weekly strangles with daywise entry, SL, and expiry logic | Derivatives (India) | [nifty-positional-strangle](./nifty-positional-strangle) |
| 🔄 Nifty Mean Reversion | 6 variations tested using Bollinger Bands, RSI, and SMA crossovers | Index (India) | [nifty-mean-reversion](./nifty-mean-reversion) |
| 💹 BTC Trend Strategy *(Planned)* | Momentum-based long/short model on Bitcoin | Crypto | _TBD_ |
| 🌍 Multi-asset Pairs Trading *(Planned)* | Statistical arbitrage between correlated assets | Global Equities | _TBD_ |


---

## 🚀 Features

- ✅ Realistic backtesting with 1-min and daily OHLC data
- 📊 Performance reports, PnL charts, and cumulative returns
- 🧠 Strategy logic explained clearly in README + Jupyter Notebooks
- 🌐 Indian and Global markets: Equity, Options, Crypto, and more

---

## 🔧 Requirements

Each sub-repo has its own `requirements.txt` or setup guide. Most projects rely on:

- Python 3.10+
- Pandas, Matplotlib, Numpy, Seaborn
- Jupyter Lab / VS Code / PyCharm

---

## 👨‍💻 Author

Arindam Das  
[GitHub](https://github.com/adas-quant) | [LinkedIn](https://www.linkedin.com/in/arindam-das-810726b8/)

---

## 📌 Note

This portfolio is under active development. New strategies and updates will be added regularly.

