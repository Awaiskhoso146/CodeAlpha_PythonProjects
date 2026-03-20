# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOGLE": 1500
}

total_value = 0

print("Available Stocks: ",list(stock_prices.keys()))

n = int(input("How many different stocks do you want to add?: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value
    else:
        print("Stock not available in database")
    
    print("Total Investment Value:",total_value)

    with open("portfolio_value.txt", "w") as file:
        file.write("Total Investment Value: " + str(total_value))

