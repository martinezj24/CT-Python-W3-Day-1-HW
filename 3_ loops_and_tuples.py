# Task 1: Stock Market Data Analysis

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ('CT', '2022-03-25', 330.2),
    ('CT', '2020-04-29', 112.0)
]

def average(stock_data, symbol):
    total = 0
    i = 0

    for data in stock_data:
        if data[0] == symbol:
            total += data[2]
            i += 1
    if i == 0:
        return None
    else:
        return total / i

