# 🧲 Nifty Positional Weekly Strangle

This strategy sells ATM CE and PE options on Nifty **every Thursday EOD** for the next week's expiry, and exits on **Wednesday EOD**, or earlier if stop-loss hits.

---

## Strategy Logic

- **Entry:** Thursday close (weekly expiry setup)
- **Exit:** Next Wednesday close, or earlier if SL hits
- **Stop Loss:** 2x individual leg premium
- **Why Wednesday Exit?** Avoids expiry-day margin spike due to SEBI regulations

---

## Status

🚧 Code structure ready  
🧪 Awaiting clean historical options dataset for real backtest  
📂 Using dummy CSV structure in `data/` folder for now
