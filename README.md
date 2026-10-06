# Stock Price Analyzer

A Python-based stock market analysis tool that fetches real-time stock data and performs comprehensive financial analysis including price trends, volatility, and moving averages.

## Features

✅ **Real-Time Data Fetching** - Download historical stock data using yfinance  
✅ **Price Analysis** - Current, average, min, and max prices with price range  
✅ **Return Metrics** - Calculate total returns and annualized volatility  
✅ **Moving Averages** - 50-day and 200-day moving average analysis  
✅ **Trend Identification** - Bullish/Bearish signals based on technical indicators  
✅ **Multi-Stock Support** - Analyze multiple stocks in one run  
✅ **Professional Reports** - Formatted, readable analysis output  

## Technologies Used

- **Python 3** - Core language
- **yfinance** - Yahoo Finance API wrapper for stock data
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations for volatility calculations

## Installation

```bash
# Clone the repository
git clone https://github.com/leoandtaby-blip/stock-price-analyzer.git
cd stock-price-analyzer

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from stock_analyzer import StockAnalyzer

# Analyze Apple stock for the past year
analyzer = StockAnalyzer('AAPL', period='1y')
analyzer.generate_report()
```

### Analyze Multiple Stocks

```python
stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']

for stock in stocks:
    analyzer = StockAnalyzer(stock, period='1y')
    analyzer.generate_report()
```

### Available Periods

- `1d` - 1 day
- `5d` - 5 days
- `1mo` - 1 month
- `3mo` - 3 months
- `6mo` - 6 months
- `1y` - 1 year (default)
- `2y` - 2 years
- `5y` - 5 years
- `10y` - 10 years
- `max` - Maximum available history

## Output Example

```
============================================================
STOCK ANALYSIS REPORT: AAPL
Period: 1y | Generated: 2026-10-06 10:30:45
============================================================

📊 PRICE ANALYSIS
------------------------------------------------------------
  Current Price.............................. $235.67
  Average Price.............................. $189.45
  Min Price.................................. $145.23
  Max Price.................................. $245.89
  Price Range................................ $100.66

📈 RETURNS & VOLATILITY
------------------------------------------------------------
  Total Return............................... +24.32%
  Annualized Volatility...................... 28.45%
  Start Price................................ $189.87
  Current Price.............................. $235.67

🎯 MOVING AVERAGES (50-Day & 200-Day)
------------------------------------------------------------
  50-Day MA.................................. $232.15
  200-Day MA................................. $198.34
  Current vs 50-Day.......................... +1.52%
  Current vs 200-Day......................... +18.79%

💡 QUICK INSIGHT
------------------------------------------------------------
  Trend: BULLISH - Price is above 50-day moving average

============================================================
```

## Key Metrics Explained

### Price Analysis
- **Current Price** - Latest closing price
- **Average Price** - Mean closing price over the period
- **Min/Max Price** - Lowest and highest prices in period
- **Price Range** - Difference between max and min

### Returns & Volatility
- **Total Return** - Percentage gain/loss from start to current
- **Annualized Volatility** - Risk measure; higher = more volatile
- **Start Price** - Opening price at start of period
- **Current Price** - Latest price

### Moving Averages
- **50-Day MA** - Short-term trend indicator
- **200-Day MA** - Long-term trend indicator
- **% vs MA** - How far current price is from the moving average

### Trend Signal
- **BULLISH** - Price above 50-day MA (uptrend)
- **BEARISH** - Price below 50-day MA (downtrend)

## Project Structure

```
stock-price-analyzer/
├── stock_analyzer.py      # Main analyzer class
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore patterns
```

## Skills Demonstrated

✓ API Integration - Fetching real-world financial data  
✓ Data Analysis - Processing and analyzing large datasets  
✓ Financial Calculations - Returns, volatility, moving averages  
✓ Object-Oriented Design - Clean, reusable class structure  
✓ Error Handling - Robust data fetching with error management  
✓ Data Visualization (Text-based) - Professional report formatting  

## Future Enhancements

- Add visualization with matplotlib/plotly
- Support for portfolio analysis
- Email alerts for price milestones
- CSV export functionality
- Technical indicators (RSI, MACD, Bollinger Bands)
- Stock comparison tools
- Backtesting strategies

## Limitations

- Requires internet connection to fetch data
- Historical data dependent on yfinance availability
- Past performance does not guarantee future results
- For educational and research purposes only

## Disclaimer

This tool is for educational purposes only. Stock market analysis is complex and involves risks. Always do your own research and consult with financial advisors before making investment decisions.

## License

MIT License - Feel free to use this project for learning and personal projects.

## Author

James (leoandtaby-blip)  
Entry-level Data/AI Engineer | Python Developer

---

Built to demonstrate data engineering and financial analysis skills. 📊📈
