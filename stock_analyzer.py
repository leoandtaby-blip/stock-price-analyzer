import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class StockAnalyzer:
    def __init__(self, symbol, period='1y'):
        """Initialize analyzer with stock symbol and period"""
        self.symbol = symbol.upper()
        self.period = period
        self.data = None
        self.analysis = {}

    def fetch_data(self):
        """Fetch historical stock data"""
        print(f"Fetching data for {self.symbol}...")
        try:
            self.data = yf.download(self.symbol, period=self.period, progress=False)
            print(f"✓ Successfully fetched {len(self.data)} trading days of data")
            return True
        except Exception as e:
            print(f"✗ Error fetching data: {e}")
            return False

    def analyze_prices(self):
        """Analyze price statistics"""
        if self.data is None:
            return None

        closing_prices = self.data['Close']

        analysis = {
            'Current Price': f"${closing_prices.iloc[-1]:.2f}",
            'Average Price': f"${closing_prices.mean():.2f}",
            'Min Price': f"${closing_prices.min():.2f}",
            'Max Price': f"${closing_prices.max():.2f}",
            'Price Range': f"${closing_prices.max() - closing_prices.min():.2f}",
        }

        return analysis

    def calculate_returns(self):
        """Calculate return metrics"""
        if self.data is None:
            return None

        closing_prices = self.data['Close']
        start_price = closing_prices.iloc[0]
        current_price = closing_prices.iloc[-1]

        total_return = ((current_price - start_price) / start_price) * 100

        # Daily returns for volatility
        daily_returns = closing_prices.pct_change().dropna()
        volatility = daily_returns.std() * np.sqrt(252) * 100  # Annualized volatility

        analysis = {
            'Total Return': f"{total_return:+.2f}%",
            'Annualized Volatility': f"{volatility:.2f}%",
            'Start Price': f"${start_price:.2f}",
            'Current Price': f"${current_price:.2f}",
        }

        return analysis

    def calculate_moving_averages(self):
        """Calculate moving averages"""
        if self.data is None:
            return None

        closing_prices = self.data['Close']
        ma_50 = closing_prices.rolling(window=50).mean().iloc[-1]
        ma_200 = closing_prices.rolling(window=200).mean().iloc[-1]
        current_price = closing_prices.iloc[-1]

        analysis = {
            '50-Day MA': f"${ma_50:.2f}",
            '200-Day MA': f"${ma_200:.2f}",
            'Current vs 50-Day': f"{((current_price - ma_50) / ma_50 * 100):+.2f}%",
            'Current vs 200-Day': f"{((current_price - ma_200) / ma_200 * 100):+.2f}%",
        }

        return analysis

    def generate_report(self):
        """Generate complete analysis report"""
        if not self.fetch_data():
            return

        print("\n" + "="*60)
        print(f"STOCK ANALYSIS REPORT: {self.symbol}")
        print(f"Period: {self.period} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60 + "\n")

        # Price Analysis
        print("📊 PRICE ANALYSIS")
        print("-" * 60)
        prices = self.analyze_prices()
        for key, value in prices.items():
            print(f"  {key:.<40} {value}")

        # Returns Analysis
        print("\n📈 RETURNS & VOLATILITY")
        print("-" * 60)
        returns = self.calculate_returns()
        for key, value in returns.items():
            print(f"  {key:.<40} {value}")

        # Moving Averages
        print("\n🎯 MOVING AVERAGES (50-Day & 200-Day)")
        print("-" * 60)
        mas = self.calculate_moving_averages()
        for key, value in mas.items():
            print(f"  {key:.<40} {value}")

        # Investment Insight
        print("\n💡 QUICK INSIGHT")
        print("-" * 60)
        current_price = self.data['Close'].iloc[-1]
        ma_50 = self.data['Close'].rolling(window=50).mean().iloc[-1]

        if current_price > ma_50:
            trend = "BULLISH - Price is above 50-day moving average"
        else:
            trend = "BEARISH - Price is below 50-day moving average"

        print(f"  Trend: {trend}")

        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    # Analyze multiple stocks
    stocks_to_analyze = ['AAPL', 'GOOGL', 'MSFT']

    for stock in stocks_to_analyze:
        analyzer = StockAnalyzer(stock, period='1y')
        analyzer.generate_report()
        print()
