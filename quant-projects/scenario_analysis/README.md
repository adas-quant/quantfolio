# ⚠️ Scenario Analysis: Stress-Testing Option Strategies

This module simulates extreme market conditions to test how option strategies behave under stress.

### 📌 Included Scenarios:
- `vol_spike_short_strangle.ipynb`: Spike implied volatility from 14% to 30% and measure MTM impact on short strangle.
- `directional_crash_long_call.ipynb`: Simulate gap-down event and analyze delta-hedged long option exposure.
- `interest_rate_shift_bond_portfolio.ipynb`: Model VaR under parallel and non-parallel shifts in the yield curve.
- `regime_switching_strategy.ipynb`: Evaluate performance across low/high volatility regimes.
- `liquidity_drain_simulation.ipynb`: Test effects of slippage and bid-ask widening.

### 🧠 Quant Concepts:
- Scenario-based VaR
- Stress MTM estimation
- IV sensitivity
- Delta/PnL decomposition

> 📚 Goal: Simulate and visualize tail risks before they hit your portfolio.
