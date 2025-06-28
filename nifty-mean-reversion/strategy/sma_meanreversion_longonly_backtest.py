# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load data
# df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=2)
# df.rename(columns={'Price': 'Date'}, inplace=True)
# df['Date'] = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)
#
# # Calculate 20 and 50 day SMAs
# df['SMA20'] = df['Close'].rolling(window=20).mean()
# df['SMA50'] = df['Close'].rolling(window=50).mean()
#
# # Drop rows with NaNs in SMA columns
# df.dropna(subset=['SMA20', 'SMA50'], inplace=True)
#
# # Initialize full series for strategy returns
# strategy_curve = [1]
# position = 0
# entry_price = 0
# entry_index = None
# trade_returns = []
#
# for i in range(1, len(df)):
#     today = df.iloc[i]
#     prev_value = strategy_curve[-1]
#
#     #if position == 0 and today['SMA20'] < today['SMA50']:
#     prev_day = df.iloc[i - 1]
#     if position == 0 and prev_day['SMA20'] >= prev_day['SMA50'] and today['SMA20'] < today['SMA50']:
#
#         position = 1
#         entry_price = today['Close']
#         entry_index = i
#         strategy_curve.append(prev_value)
#     elif position == 1:
#         hold_days = i - entry_index
#         if hold_days >= 10:
#             exit_price = today['Close']
#             ret = (exit_price - entry_price) / entry_price
#             trade_returns.append(ret)
#             new_value = prev_value * (1 + ret)
#             strategy_curve.append(new_value)
#             position = 0
#             entry_price = 0
#             entry_index = None
#         else:
#             strategy_curve.append(prev_value)
#     else:
#         strategy_curve.append(prev_value)
#
# # Fill any remaining days
# while len(strategy_curve) < len(df):
#     strategy_curve.append(strategy_curve[-1])
#
# # Buy & Hold
# buyhold = df['Close'] / df['Close'].iloc[0]
#
# # Plot
# plt.figure(figsize=(12, 6))
# plt.plot(df.index, strategy_curve, label='SMA Mean Reversion')
# plt.plot(df.index, buyhold, label='Buy & Hold')
# plt.title('SMA Mean Reversion vs Buy & Hold')
# plt.xlabel('Date')
# plt.ylabel('Cumulative Returns')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# #plt.savefig('../plots/sma_meanreversion_vs_buyhold.png')
# plt.show()
#
# # Performance Metrics
# strategy_curve = np.array(strategy_curve)
# returns = pd.Series(np.diff(strategy_curve) / strategy_curve[:-1])
#
# total_return = strategy_curve[-1] - 1
# num_trades = len(trade_returns)
# winning_trades = [r for r in trade_returns if r > 0]
# losing_trades = [r for r in trade_returns if r <= 0]
# win_rate = len(winning_trades) / num_trades if num_trades > 0 else 0
# avg_win = np.mean(winning_trades) if winning_trades else 0
# avg_loss = np.mean(losing_trades) if losing_trades else 0
# sharpe = returns.mean() / returns.std() * np.sqrt(252) if returns.std() > 0 else 0
#
# # Max drawdown
# cumulative = pd.Series(strategy_curve)
# rolling_max = cumulative.cummax()
# drawdown = (cumulative - rolling_max) / rolling_max
# max_dd = drawdown.min()
#
# print("\nPerformance Metrics")
# print("====================")
# print(f"Total Return       : {total_return:.2%}")
# print(f"No. of Trades      : {num_trades}")
# print(f"Win Rate           : {win_rate:.2%}")
# print(f"Avg Winning Return : {avg_win:.2%}")
# print(f"Avg Losing Return  : {avg_loss:.2%}")
# print(f"Max Drawdown       : {max_dd:.2%}")
# print(f"Sharpe Ratio       : {sharpe:.2f}")


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load data
df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=2)
df.rename(columns={'Price': 'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate 20 and 50 day SMAs
df['SMA20'] = df['Close'].rolling(window=20).mean()
df['SMA50'] = df['Close'].rolling(window=50).mean()

# Drop rows with NaNs in SMA columns
df.dropna(subset=['SMA20', 'SMA50'], inplace=True)

# Initialize full series for strategy returns
strategy_curve = [1]
position = 0
entry_price = 0
entry_index = None
trade_returns = []
trade_log = []

for i in range(1, len(df)):
    today = df.iloc[i]
    prev_value = strategy_curve[-1]

    prev_day = df.iloc[i - 1]
    if position == 0 and prev_day['SMA20'] >= prev_day['SMA50'] and today['SMA20'] < today['SMA50']:
        position = 1
        entry_price = today['Close']
        entry_index = i
        entry_date = df.index[i]
        strategy_curve.append(prev_value)
    elif position == 1:
        hold_days = i - entry_index
        if hold_days >= 10:
            exit_price = today['Close']
            ret = (exit_price - entry_price) / entry_price
            trade_returns.append(ret)
            new_value = prev_value * (1 + ret)
            strategy_curve.append(new_value)
            exit_date = df.index[i]

            trade_log.append({
                'Entry Date': entry_date.strftime('%Y-%m-%d'),
                'Exit Date': exit_date.strftime('%Y-%m-%d'),
                'Entry Price': round(entry_price, 2),
                'Exit Price': round(exit_price, 2),
                'Return (%)': round(ret * 100, 2)
            })

            position = 0
            entry_price = 0
            entry_index = None
        else:
            strategy_curve.append(prev_value)
    else:
        strategy_curve.append(prev_value)

# Fill any remaining days
while len(strategy_curve) < len(df):
    strategy_curve.append(strategy_curve[-1])

# Buy & Hold
buyhold = df['Close'] / df['Close'].iloc[0]

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, strategy_curve, label='SMA Mean Reversion')
plt.plot(df.index, buyhold, label='Buy & Hold')
plt.title('SMA Mean Reversion vs Buy & Hold')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../plots/sma_meanreversion_longonly_vs_buyhold.png')
plt.show()

# Performance Metrics
strategy_curve = np.array(strategy_curve)
returns = pd.Series(np.diff(strategy_curve) / strategy_curve[:-1])

total_return = strategy_curve[-1] - 1
num_trades = len(trade_returns)
winning_trades = [r for r in trade_returns if r > 0]
losing_trades = [r for r in trade_returns if r <= 0]
win_rate = len(winning_trades) / num_trades if num_trades > 0 else 0
avg_win = np.mean(winning_trades) if winning_trades else 0
avg_loss = np.mean(losing_trades) if losing_trades else 0
sharpe = returns.mean() / returns.std() * np.sqrt(252) if returns.std() > 0 else 0

# Max drawdown
cumulative = pd.Series(strategy_curve)
rolling_max = cumulative.cummax()
drawdown = (cumulative - rolling_max) / rolling_max
max_dd = drawdown.min()

print("\nPerformance Metrics")
print("====================")
print(f"Total Return       : {total_return:.2%}")
print(f"No. of Trades      : {num_trades}")
print(f"Win Rate           : {win_rate:.2%}")
print(f"Avg Winning Return : {avg_win:.2%}")
print(f"Avg Losing Return  : {avg_loss:.2%}")
print(f"Max Drawdown       : {max_dd:.2%}")
print(f"Sharpe Ratio       : {sharpe:.2f}")

# Save trade logs
result_dir = '../results'
os.makedirs(result_dir, exist_ok=True)
trade_log_df = pd.DataFrame(trade_log)
trade_log_df.to_csv(os.path.join(result_dir, 'sma_meanreversion_longonly_trades.csv'), index=False)
print("\nTrade log saved to results/sma_meanreversion_longonly_trades.csv")
