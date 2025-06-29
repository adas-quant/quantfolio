# 📊 Quantfolio: A Portfolio of Quantitative Trading Strategies & Research Demos

![GitHub last commit](https://img.shields.io/github/last-commit/adas-quant/quantfolio)
![GitHub repo size](https://img.shields.io/github/repo-size/adas-quant/quantfolio)
![GitHub license](https://img.shields.io/github/license/adas-quant/quantfolio)

Welcome to **Quantfolio** — a curated collection of algorithmic trading strategies and quantitative finance notebooks developed using Python.

This project demonstrates both:
- 📈 Live-market backtested strategies across Indian F&O and equities
- 🧪 Quant research tools — pricing models, stress testing, and trade analytics

---

## 🗂 Table of Contents

- [Strategies](#-strategies)
- [Quant Research & Risk Demos](#-quant-research--risk-demos)
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

## 🧠 Quant Research & Risk Demos

Notebooks and tools that demonstrate option pricing, stress-test strategies under market shocks, and analyze trade performance.

| Folder | Description |
|--------|-------------|
| `quant-projects/option-pricing/` | Black-Scholes, Binomial Trees, and Monte Carlo pricing models using QuantLib & NumPy |
| `quant-projects/scenario_analysis/` | Stress-test option strategies under volatility spikes, directional crashes, regime shifts, and more |
| `quant-projects/trade_analytics/` | Analyze trade logs with MTM, PnL, Sharpe, drawdown, win/loss histograms & strategy filters |


---

## 🚀 Features

- ✅ Realistic backtesting with 1-min and daily OHLC data
- 📊 Performance reports, PnL charts, and cumulative returns
- 🧠 Strategy logic + pricing models explained via clean Jupyter notebooks
- 🌐 Indian and Global markets: Equity, Options, Crypto, and more

---

## 🔧 Requirements

Each sub-repo has its own `requirements.txt`. Most projects use:

- Python 3.10+
- Pandas, Matplotlib, NumPy, Seaborn
- QuantLib (`quantlib-python`)
- ipywidgets (for interactive pricing demos)
- Jupyter Lab / VS Code / PyCharm

---

## 👨‍💻 Author

Arindam Das  
[GitHub](https://github.com/adas-quant) | [LinkedIn](https://www.linkedin.com/in/arindam-das-810726b8/)

---

## 📌 Note

This portfolio is under active development. New strategies and quant notebooks will be added regularly.
