import pandas as pd
import matplotlib.pyplot as plt

# Load Nifty data
# df = pd.read_csv('../data/nifty_daily_data.csv', parse_dates=['Date'])
# df.set_index('Date', inplace=True)


# df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=3, parse_dates=['Price'])
# df.rename(columns={'Price': 'Date'}, inplace=True)
# df.set_index('Date', inplace=True)

# Skip first 2 rows only (row 3 is actually the header)
# df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=2)
#
# # Rename 'Price' to 'Date'
# df.rename(columns={'Price': 'Date'}, inplace=True)
#
# # Convert 'Date' to datetime
# df['Date'] = pd.to_datetime(df['Date'])
#
# # Set 'Date' as index
# df.set_index('Date', inplace=True)
# print(df.columns)


# Step 1: Read and clean data
df = pd.read_csv('../data/nifty_daily_data.csv', skiprows=2)

# Step 2: Parse 'Date' column properly
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Set 'Date' as index
df.set_index('Date', inplace=True)


# Calculate Bollinger Bands
df['20SMA'] = df['Close'].rolling(window=20).mean()
df['20STD'] = df['Close'].rolling(window=20).std()

df['UpperBand'] = df['20SMA'] + 2 * df['20STD']
df['LowerBand'] = df['20SMA'] - 2 * df['20STD']

# Generate Buy/Sell Signals
df['Position'] = 0
df.loc[df['Close'] < df['LowerBand'], 'Position'] = 1   # Buy signal
df.loc[df['Close'] > df['UpperBand'], 'Position'] = -1  # Sell signal

# Shift positions for next day execution
df['Strategy'] = df['Position'].shift(1) * df['Close'].pct_change()

# Cumulative returns
df['Strategy_Cum'] = (1 + df['Strategy']).cumprod()
df['Market_Cum'] = (1 + df['Close'].pct_change()).cumprod()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Strategy_Cum'], label='Strategy')
plt.plot(df.index, df['Market_Cum'], label='Buy & Hold', linestyle='--')
plt.title("Nifty Mean Reversion Strategy vs Buy & Hold")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('../plots/bollinger_vs_buyhold.png', dpi=300)
plt.show()
