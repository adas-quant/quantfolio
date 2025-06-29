# 📊 Trade Analytics & Journal Tracker

Analyze your personal trading performance using real broker CSV data — turn raw trade logs into insights.

### 🧰 Components:
- `journal_parser.py`: Reads raw broker CSV and cleans it into structured trades.
- `metrics_calculator.py`: Computes P&L, MTM, exposure, Sharpe Ratio, max drawdown, win/loss %, etc.
- `trade_dashboard.ipynb`: Visualizes trade history with equity curves, histograms, pie charts.
- `strategy_filtering.ipynb`: Slice performance by strategy, holding time, day-of-week, tags.
- `export_report.py`: [Planned] Export summary to Excel/PDF

### 📁 Data Files:
- `broker_sample.csv`: Input (raw)
- `processed_trades.csv`: Output (cleaned)

### 🧠 Why This Exists:
Trading is not just execution — it's iteration. This module helps track what’s working, what’s not, and how to improve systematically.

> 📚 Goal: Build your own version of a professional PnL engine — personalized for your tradebook.
