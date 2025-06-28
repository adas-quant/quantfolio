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

# Buy when RSI < 30 (oversold), sell when RSI > 45 or after holding for max 10 days

# position = 0
# entry_price = 0
# entry_index = None
# returns = []
#
# for i in range(1, len(df)):
#     if position == 0 and df['RSI'].iloc[i] < 40:
#         position = 1
#         entry_price = df['Close'].iloc[i]
#         entry_index = i
#     elif position == 1:
#         hold_days = i - entry_index
#         if df['RSI'].iloc[i] > 60 or hold_days >= 10:
#             exit_price = df['Close'].iloc[i]
#             returns.append((exit_price - entry_price) / entry_price)
#             position = 0
#             entry_price = 0
#             entry_index = None
#
# # If still in position at end
# if position == 1:
#     exit_price = df['Close'].iloc[-1]
#     returns.append((exit_price - entry_price) / entry_price)
#
# strategy_returns = np.cumprod([1 + r for r in returns])
# buyhold_returns = df['Close'] / df['Close'].iloc[0]

# Initialize
position = 0
entry_price = 0
entry_index = None
strategy_curve = [1]  # Start with initial capital of 1
current_value = 1

# Track cumulative returns
for i in range(1, len(df)):
    if position == 0 and df['RSI'].iloc[i] < 30:
        position = 1
        entry_price = df['Close'].iloc[i]
        entry_index = i
    elif position == 1:
        hold_days = i - entry_index
        if df['RSI'].iloc[i] > 60 or hold_days >= 10:
            exit_price = df['Close'].iloc[i]
            ret = (exit_price - entry_price) / entry_price
            current_value *= (1 + ret)
            position = 0
            entry_price = 0
            entry_index = None
    strategy_curve.append(current_value)

# Ensure curve length matches index
strategy_returns = pd.Series(strategy_curve, index=df.index[:len(strategy_curve)])
buyhold_returns = df['Close'] / df['Close'].iloc[0]


# Plot
plt.figure(figsize=(12, 6))
# plt.plot(df.index[:len(strategy_returns)], strategy_returns, label='RSI Strategy')
plt.plot(df.index, strategy_returns, label='RSI Mean Reversion Strategy')
plt.plot(df.index, buyhold_returns, label='Buy & Hold')
plt.title('RSI Mean Reversion Strategy vs Buy & Hold')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('../plots/rsi_mean_reversion_vs_buyhold.png')
plt.show()
