# 🧠 Black-Scholes Option Pricing — In Depth

This document provides a theoretical and practical overview of the **Black-Scholes Model**, including key assumptions, pricing formula, sensitivities (Greeks), and implementation notes using QuantLib in Python.

---

## 🧾 1. Overview

The **Black-Scholes-Merton (BSM)** model is a foundational tool in quantitative finance for pricing **European-style options**.  
It provides a closed-form solution under several key assumptions.

Developed by **Fischer Black**, **Myron Scholes**, and later extended by **Robert Merton**, this model earned a Nobel Prize and remains central in modern derivatives pricing.

---

## ⚙️ 2. Formulae

### Call Option Price:
$$ C = S_0 N(d_1) - K e^{-rT} N(d_2) $$

### Put Option Price:
$$ P = K e^{-rT} N(-d_2) - S_0 N(-d_1) $$

Where:

- \( d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}} \)
- \( d_2 = d_1 - \sigma \sqrt{T} \)

And:
- \( S_0 \): Spot price
- \( K \): Strike price
- \( T \): Time to maturity (in years)
- \( r \): Risk-free interest rate
- \( \sigma \): Volatility
- \( N(x) \): Cumulative distribution function of standard normal

---

## 🧩 3. Assumptions

- Log-normal distribution of asset prices
- Constant volatility and interest rate
- No arbitrage, no transaction costs
- European-style exercise only (at expiry)
- Continuous trading and hedging

---

## 📉 4. Greeks (Sensitivities)

| Greek | Meaning | Behavior |
|-------|---------|----------|
| Delta | Sensitivity to underlying asset price | \( \Delta = N(d_1) \) for calls |
| Gamma | Sensitivity of Delta to price | Second derivative |
| Vega | Sensitivity to volatility | Peaks at ATM options |
| Theta | Time decay | Negative for long options |
| Rho   | Sensitivity to interest rate | More significant for longer maturities |

> Our notebook implementation shows how price changes with these inputs interactively.

---

## 🧪 5. QuantLib Implementation

In our [notebook](../option_pricing/quantlib_black_scholes.ipynb), we use:

- `QuantLib.BlackScholesMertonProcess` to simulate underlying dynamics
- `QuantLib.EuropeanOption` with payoff and exercise
- Sliders via `ipywidgets` to dynamically update inputs and see real-time pricing

The model is **non-path dependent**, so closed-form pricing is efficient.

---

## 📌 6. Limitations in Practice

- Real options markets show **implied volatility smiles/skews** — BSM assumes constant σ
- **American options**, which allow early exercise, need numerical methods (e.g. binomial tree)
- BSM does not handle **jumps** or **discrete dividends** well
- Still widely used as a benchmark or for implied volatility estimation

---

## 📚 7. References

- "Options, Futures, and Other Derivatives" – John Hull
- QuantLib Documentation: https://www.quantlib.org/
- Investopedia: Black-Scholes Model
- Original paper: Black, F., and Scholes, M. (1973)

---

*Last updated: 29th June 2025 by Arindam Das*
