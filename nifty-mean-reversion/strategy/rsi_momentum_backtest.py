import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=2)
df.rename(columns={'Price': 'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate 14-day RSI
delta = df['Close'].diff()
gain = np.where(delta > 0, delta, 0)
loss = np.where(delta < 0, -delta, 0)

avg_gain = pd.Series(gain).rolling(window=14).mean()
avg_loss = pd.Series(loss).rolling(window=14).mean()

rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))
df['RSI'] = rsi.values

# Buy when RSI > 60 (momentum), sell when RSI < 55 or after max 10 days
position = 0
entry_price = 0
entry_index = None
strategy_curve = [1]
current_value = 1

for i in range(1, len(df)):
    if position == 0 and df['RSI'].iloc[i] > 60:
        position = 1
        entry_price = df['Close'].iloc[i]
        entry_index = i
    elif position == 1:
        hold_days = i - entry_index
        if df['RSI'].iloc[i] < 55 or hold_days >= 10:
            exit_price = df['Close'].iloc[i]
            ret = (exit_price - entry_price) / entry_price
            current_value *= (1 + ret)
            position = 0
            entry_price = 0
            entry_index = None
    strategy_curve.append(current_value)

strategy_returns = pd.Series(strategy_curve, index=df.index[:len(strategy_curve)])
buyhold_returns = df['Close'] / df['Close'].iloc[0]

plt.figure(figsize=(12, 6))
plt.plot(df.index, strategy_returns, label='RSI Momentum Strategy (RSI>60)')
plt.plot(df.index, buyhold_returns, label='Buy & Hold')
plt.title('RSI Momentum Strategy vs Buy & Hold')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('../plots/rsi_momentum_vs_buyhold.png')
plt.show()
