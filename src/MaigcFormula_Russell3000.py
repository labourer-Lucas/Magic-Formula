import yfinance as yf
import pandas as pd
stock_data = pd.read_csv("data\Russell-3000.csv")

# Assume the CSV file contains a column named 'Ticker' with stock symbols
stocks = stock_data['ticker'].tolist()

# Optionally, use yfinance to get market cap for validation or additional data
# market_caps = []
# # Define the stock tickers
# stocks = ["AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "DIS", "DOW", "XOM",
#           "HD", "IBM", "INTC", "JNJ", "KO", "MCD", "MMM", "MRK", "MSFT",
#           "NKE", "PFE", "PG", "TRV", "UNH", "VZ", "V", "WMT", "WBA","TSLA","HTHT"]
# stocks = ["AAPL"]
# Dictionary to store thenvalues
stockLength=len(stocks)
stockCount=0
data = []
# Loop through each stock ticker
for ticker in stocks:
    stockCount=stockCount+1
    try:
        # Fetch the financial data using yfinance
        stock = yf.Ticker(ticker)
        # Get the income statement (quarterly or yearly)
        income_statement = stock.financials  # 'quarterly_financials' for quarterly data
        # print(income_statement)
        if income_statement is not None and not income_statement.empty:
            try:
                # Calculate EBIT as Operating Income (EBIT) = Total Revenue - Total Operating Expenses
                # EBIT = Net Income + Interest Expense + Income Tax Expense (If available)
                latest_ebit = income_statement.loc['EBIT'].iloc[0]
                # print(f"{ticker}'s EBIT is {latest_ebit}")
            except KeyError:
                latest_ebit = None
        else:
            latest_ebit = None
        balance_sheet = stock.balance_sheet
        # print(balance_sheet.index)
        if balance_sheet is not None and not balance_sheet.empty:
            try:
                # Calculate EBIT as Operating Income (EBIT) = Total Revenue - Total Operating Expenses
                # EBIT = Net Income + Interest Expense + Income Tax Expense (If available)
                total_current_assets = balance_sheet.loc['Total Assets'].iloc[0]-balance_sheet.loc['Total Non Current Assets'].iloc[0]
                current_liabilities=balance_sheet.loc['Current Liabilities'].iloc[0]
                net_ppe=balance_sheet.loc['Net PPE'].iloc[0]
            except KeyError:
                total_current_assets = None
        else:
            total_current_assets = None
        # Get the current stock price
        current_price = stock.history(period="1d")['Close'].iloc[0]
        # Get the EPS (TTM) from the financial data
        eps_ttm = stock.info['trailingEps']
        # Calculate Earnings Yield
        earnings_yield = (eps_ttm / current_price) 
        data.append({'Ticker': ticker, 'EBIT': latest_ebit,'Total current asstes':total_current_assets,'Current Liabilities':current_liabilities,'Net PPE':net_ppe,'Earning Yields':earnings_yield})
        print("Data successfully scraped for ", ticker,"No. ",stockCount," of ",stockLength)
    except:
        print("Problem scraping data for ",ticker)

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)
nan_rows = data_df[data_df.isna().any(axis=1)]
print("Rows with NaN values:\n", nan_rows)
# Step 2: Drop rows with any NaN values
data_df = data_df.dropna()
# calculate return on capital
data_df["ROC"]=data_df["EBIT"]/(data_df["Net PPE"]+data_df["Total current asstes"]-data_df["Current Liabilities"])
# Display the DataFrame
print("\n DataFrame:")
print(data_df)
stocks_index = data_df.columns
print(stocks_index)
data_df_rank = data_df
data_df_rank["Earning Yields Rank"]=data_df_rank["Earning Yields"].rank(ascending=False,na_option='bottom')
data_df_rank["ROC rank"]=data_df_rank["ROC"].rank(ascending=False,na_option='bottom')
data_df_rank["CombRank"] = data_df_rank["Earning Yields"].rank(ascending=False,na_option='bottom')+data_df_rank["ROC"].rank(ascending=False,na_option='bottom')
data_df_rank["MagicFormulaRank"] = data_df_rank["CombRank"].rank(method='first')
value_stocks = data_df_rank.sort_values("MagicFormulaRank")
print("------------------------------------------------")
print("Value stocks based on Greenblatt's Magic Formula")
df = value_stocks.fillna(0)
print(df)
file_path = "magic_formula_rank.xlsx"  # Replace with your desired file path
# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)
print(f"DataFrame saved to {file_path}")