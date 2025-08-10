import yfinance as yf
import os

def fetch_and_save_yfinance_data(tickers, start_date, end_date):
    """
    Fetches historical financial data for a list of tickers using yfinance
    and saves the raw data to the 'data/raw/' directory. This version
    downloads tickers sequentially to avoid database locking errors.
    
    This script is intended to be run once from the command line.
    """
    print(f"Starting sequential download for {tickers}...")

    # Create directory if it doesn't exist
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')
        print("Created directory: data/raw/")

    for ticker in tickers:
        print(f"--- Downloading data for {ticker} from {start_date} to {end_date} ---")
        try:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)

            if data.empty:
                print(f"No data fetched for {ticker}. Skipping.")
                continue

            output_path = f'data/raw/{ticker.lower()}_raw.csv'
            data.to_csv(output_path)
            print(f"Successfully saved raw data for {ticker} to {output_path}")
        except Exception as e:
            print(f"An error occurred while fetching data for {ticker}: {e}")
    
    print("\nAll downloads complete.")

if __name__ == '__main__':
    TICKERS = ['TSLA', 'SPY', 'BND']
    START_DATE = '2015-07-01'
    END_DATE = '2025-07-31'
    
    fetch_and_save_yfinance_data(TICKERS, START_DATE, END_DATE)