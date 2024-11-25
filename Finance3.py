import pandas as pd
###Creating Series and DataFrames
##Creating a Series
# Create a Series for stock prices
stock_prices = pd.Series([100, 150, 200], index=['Stock A', 'Stock B', 'Stock C'])
print(stock_prices)