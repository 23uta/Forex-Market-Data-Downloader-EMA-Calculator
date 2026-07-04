# Forex Market Data Downloader & EMA Calculator

An automated Python data acquisition and preprocessing utility designed for algorithmic trading systems. This tool connects directly to the Yahoo Finance API to fetch high-resolution, historical 5-minute interval market data for Gold futures (`GC=F`), cleans and formats the structure, saves it into a standardized CSV file, and computes Exponential Moving Averages (EMA).

This script serves as the primary **Data Ingestion pipeline** for the Gold Scanner and Backtester engine.

## 🚀 Features

- **Automated Data Fetching:** Downloads 60 days of historical 5-minute interval candlestick data for Gold (`GC=F`) via `yfinance`.
- **Data Restructuring & Cleaning:** Resets index formats and explicitly flattens column multi-indexes into standard OHLCV (Open, High, Low, Close, Volume) structures.
- **Local Storage Management:** Exports the fully formatted market data matrix into a `gold_5m_full_table.csv` file ready for analytical pipelines.
- **Technical Indicator Computation:** Calculates a 50-period Exponential Moving Average (EMA 50) based on closing prices to identify baseline market trends.

## 🛠️ Tech Stack & Requirements

The tool uses light, industry-standard data libraries:
- **yfinance** - For reliable financial market data streaming and retrieval.
- **Pandas** - For matrix manipulation, mathematical calculations, and CSV serialization.

## 📦 Quick Start & Setup

1. **Create the Repository Files:**
   Create a new file in your GitHub repository named `README.md` and paste this content inside it.

2. **Install Dependencies:**
   Ensure you have the required libraries installed on your machine:

   <<< pip install yfinance pandas>>> 

3. **Data Preparation & Ingestion:**
Place the Python script (e.g., `download_data.py`) in your project root directory.

## 📈 Execution

Run the script from your terminal to fetch the latest market data:


<<< python main.py >>>


### Expected Output:

Upon execution, the terminal will display a clean matrix snapshot of the latest computed EMA values and confirm storage deployment:

```text
                  Close        EMA50
Datetime                            
2026-07-04 16:15  2345.50  2342.10
2026-07-04 16:20  2346.10  2342.25
2026-07-04 16:25  2344.80  2342.35

 Success! The table is saved to 'gold_5m_full_table.csv'.

```

## 🔗 Project Integration

This downloader generates the precise `gold_5m_full_table.csv` matrix required to feed the main market momentum scanner, automating your entire quantitative trading workflow from ingestion to backtesting.
