# nse_option_chain_scraper.py

import requests
import pandas as pd

def fetch_nse_option_chain(symbol="NIFTY"):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain",
        "X-Requested-With": "XMLHttpRequest"
    }

    session = requests.Session()
    session.headers.update(headers)

    # Correct cookie setup to avoid 401
    init_url = "https://www.nseindia.com/option-chain"
    session.get(init_url, timeout=5)

    # Now call the API
    response = session.get(url, timeout=5)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status: {response.status_code}")

    try:
        data = response.json()
    except Exception as e:
        raise Exception("Failed to decode JSON. NSE may have blocked the session.") from e

    calls, puts = [], []

    for record in data["records"]["data"]:
        strike = record.get("strikePrice")
        expiry = record.get("expiryDate")

        ce = record.get("CE", {})
        pe = record.get("PE", {})

        if ce:
            calls.append({
                "type": "Call",
                "expiry": expiry,
                "strike": strike,
                "IV": ce.get("impliedVolatility"),
                "LTP": ce.get("lastPrice"),
                "Volume": ce.get("totalTradedVolume")
            })
        if pe:
            puts.append({
                "type": "Put",
                "expiry": expiry,
                "strike": strike,
                "IV": pe.get("impliedVolatility"),
                "LTP": pe.get("lastPrice"),
                "Volume": pe.get("totalTradedVolume")
            })

    df_calls = pd.DataFrame(calls)
    df_puts = pd.DataFrame(puts)
    df = pd.concat([df_calls, df_puts]).sort_values(by=["expiry", "strike", "type"])

    return df.reset_index(drop=True)

# 🧪 Run
if __name__ == "__main__":
    df = fetch_nse_option_chain("NIFTY")
    print(df.head(10))
    df.to_csv("nifty_option_chain.csv", index=False)
