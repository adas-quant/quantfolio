# nifty_intraday_strangle_backtest.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Settings
ENTRY_TIME = "09:20"
EXIT_TIME = "15:20"
ENTRY_PREMIUM = 20
STOP_LOSS_MULTIPLIER = 2


# Load historical options data
def load_data(csv_path):
    df = pd.read_csv(csv_path, parse_dates=["datetime"])
    df['date'] = df['datetime'].dt.date
    df['time'] = df['datetime'].dt.time
    return df


# Filter ATM options near 9:20am with premium ≈ 20
def find_entry_options(df, entry_time):
    entry_df = df[df['time'] == pd.to_datetime(entry_time).time()]
    call = entry_df[(entry_df['option_type'] == 'CE') & (entry_df['ltp'].between(18, 22))].sort_values('ltp').head(1)
    put = entry_df[(entry_df['option_type'] == 'PE') & (entry_df['ltp'].between(18, 22))].sort_values('ltp').head(1)
    return call, put


# Backtest loop (simplified)
# def backtest(data_path):
#     df = load_data(data_path)
#     results = []
#
#     for date in df['date'].unique():
#         daily_df = df[df['date'] == date]
#         call, put = find_entry_options(daily_df, ENTRY_TIME)
#
#         if call.empty or put.empty:
#             continue  # skip if no suitable strike found
#
#         call_strike = call['strike_price'].values[0]
#         put_strike = put['strike_price'].values[0]
#
#         call_trade = daily_df[(daily_df['strike_price'] == call_strike) & (daily_df['option_type'] == 'CE')]
#         put_trade = daily_df[(daily_df['strike_price'] == put_strike) & (daily_df['option_type'] == 'PE')]
#
#         # Exit conditions and PnL logic goes here...
#
#         # For now, add dummy PnL
#         results.append({
#             "date": date,
#             "call_strike": call_strike,
#             "put_strike": put_strike,
#             "pnl": 0  # Replace with actual PnL later
#         })
#
#     return pd.DataFrame(results)

#Backtest loop updated
def backtest(data_path):
    df = load_data(data_path)
    results = []

    for date in df['date'].unique():
        daily_df = df[df['date'] == date]
        entry_df = daily_df[daily_df['time'] == pd.to_datetime(ENTRY_TIME).time()]

        call = entry_df[(entry_df['option_type'] == 'CE') & (entry_df['ltp'].between(18, 22))].sort_values('ltp').head(1)
        put = entry_df[(entry_df['option_type'] == 'PE') & (entry_df['ltp'].between(18, 22))].sort_values('ltp').head(1)

        if call.empty or put.empty:
            continue

        call_strike = call['strike_price'].values[0]
        put_strike = put['strike_price'].values[0]
        ce_entry_price = call['ltp'].values[0]
        pe_entry_price = put['ltp'].values[0]
        ce_exit_price = ce_entry_price
        pe_exit_price = pe_entry_price

        ce_df = daily_df[(daily_df['strike_price'] == call_strike) & (daily_df['option_type'] == 'CE')]
        pe_df = daily_df[(daily_df['strike_price'] == put_strike) & (daily_df['option_type'] == 'PE')]

        # Flags for SL
        ce_sl_hit = False
        pe_sl_hit = False

        # Track through the day
        for t in daily_df['time'].unique():
            time_slice_ce = ce_df[ce_df['time'] == t]
            time_slice_pe = pe_df[pe_df['time'] == t]

            if not ce_sl_hit and not time_slice_ce.empty and time_slice_ce['ltp'].values[0] >= ce_entry_price * STOP_LOSS_MULTIPLIER:
                ce_exit_price = time_slice_ce['ltp'].values[0]
                ce_sl_hit = True

            if not pe_sl_hit and not time_slice_pe.empty and time_slice_pe['ltp'].values[0] >= pe_entry_price * STOP_LOSS_MULTIPLIER:
                pe_exit_price = time_slice_pe['ltp'].values[0]
                pe_sl_hit = True

        # If leg not exited by SL, square off at 3:20 PM
        final_time = pd.to_datetime(EXIT_TIME).time()

        if not ce_sl_hit:
            last_ce = ce_df[ce_df['time'] == final_time]
            if not last_ce.empty:
                ce_exit_price = last_ce['ltp'].values[0]

        if not pe_sl_hit:
            last_pe = pe_df[pe_df['time'] == final_time]
            if not last_pe.empty:
                pe_exit_price = last_pe['ltp'].values[0]

        # PnL Calculation (since we shorted both options)
        pnl = (ce_entry_price - ce_exit_price) + (pe_entry_price - pe_exit_price)

        results.append({
            "date": date,
            "call_strike": call_strike,
            "put_strike": put_strike,
            "ce_entry": ce_entry_price,
            "ce_exit": ce_exit_price,
            "pe_entry": pe_entry_price,
            "pe_exit": pe_exit_price,
            "ce_sl_hit": ce_sl_hit,
            "pe_sl_hit": pe_sl_hit,
            "pnl": pnl
        })

    return pd.DataFrame(results)



if __name__ == "__main__":
    csv_path = "../data/nifty_sample_data.csv"  # <- Update with real file
    df = backtest(csv_path)
    df.to_csv("../plots/strangle_results.csv", index=False)
    print("Backtest complete. Results saved.")
