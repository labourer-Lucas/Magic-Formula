# Magic-Formula

This repo is an implementation of Magic Formula which is introduced in the book "The Little Book That Still Beats the Market" by Joel Greenblatt.

My implementation is largely inspired by [Greenblatt-Magic-Formula-Value-Investing](https://github.com/rbhatia46/Greenblatt-Magic-Formula-Value-Investing), however, this repo didn't update anymore. Therefore, I wrote my own one.

####  IMPORTANT LEGAL DISCLAIMER 

This repo is based on [yfinance]([ranaroussi/yfinance: Download market data from Yahoo! Finance's API (github.com)](https://github.com/ranaroussi/yfinance)): 

> yfinance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.

## [Magic Formula Definition](https://en.wikipedia.org/wiki/Magic_formula_investing)  

1. Establish a minimum [market capitalization](https://en.wikipedia.org/wiki/Market_capitalization) (usually greater than $50     million).
2. Exclude [utility](https://en.wikipedia.org/wiki/Public_utility) and [financial](https://en.wikipedia.org/wiki/Financial) stocks.
3. Exclude foreign companies ([American      Depositary Receipts](https://en.wikipedia.org/wiki/American_Depositary_Receipt)).
4. Determine company's [earnings yield](https://en.wikipedia.org/wiki/Earnings_yield) = [EBIT](https://en.wikipedia.org/wiki/Earnings_before_interest_and_taxes) / [enterprise      value](https://en.wikipedia.org/wiki/Enterprise_value).
5. Determine company's [return on capital](https://en.wikipedia.org/wiki/Return_on_capital) = [EBIT](https://en.wikipedia.org/wiki/Earnings_before_interest_and_taxes) / (net [fixed assets](https://en.wikipedia.org/wiki/Fixed_assets) + [working capital](https://en.wikipedia.org/wiki/Working_capital)).
6. Rank all companies above chosen [market capitalization](https://en.wikipedia.org/wiki/Market_capitalization) by highest earnings yield and highest return on capital (ranked as [percentages](https://en.wikipedia.org/wiki/Percentage)).
7. Invest in 20–30 highest ranked companies, accumulating 2–3 positions per month over a 12-month period.
8. Re-balance [portfolio](https://en.wikipedia.org/wiki/Portfolio_(finance)) once per year, selling losers one week before the year-mark and winners one week after the year mark.
9. Continue over a long-term (5–10+ year) period.

## Dependency

Install `yfinance` using `pip`:

```{.sourceCode
$ pip install yfinance --upgrade --no-cache-dir
```

## Quick Start

You just need to simply change the variable `stock` in `MagicFormula.py` to the company you prefer:

```python
stocks = ["AXP", "AAPL", "BA", "CAT", "CVX", "CSCO", "DIS", "DOW", "XOM",
          "HD", "IBM", "INTC", "JNJ", "KO", "MCD", "MMM", "MRK", "MSFT",
          "NKE", "PFE", "PG", "TRV", "UNH", "VZ", "V", "WMT", "WBA","TSLA","HTHT"]
```

and the run the code.

