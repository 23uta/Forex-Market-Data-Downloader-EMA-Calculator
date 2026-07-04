import yfinance as yf
import pandas as pd

# 1. Fetch 60 days of historical data at a 5-minute interval
data = yf.download("GC=F", period="60d", interval="5m", progress=False)

# 3. Convert Datetime from index to a standard dataframe column
data = data.reset_index()

# 4. Rename columns manually to ensure data structure accuracy
data.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']

# 5. Configure Pandas display settings for clear console visibility
pd.set_option('display.max_rows', 100) # Displays up to 100 rows in the Terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# 6. Print initial rows for verification (Optional)

# 7. Save the finalized dataframe into a local CSV file
data.to_csv("gold_5m_full_table.csv", index=False)

print("\n Success! The table is saved .")

#-------------------------------------------

# Uploading locally stored market data
df = pd.read_csv("gold_5m_full_table.csv")

def calculate_emas(df):
    # Calculate the 50-period Exponential Moving Average (EMA 50)
    df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()

    # Print the tail of the data to verify computed values
    print(df[['Close', 'EMA50']].tail())

    return df

calculate_emas(df)
