data = {
"cost_price": 225.89,
"sell_price": 550.00,
"eclairs": 100
}
a = data["sell_price"] - data["cost_price"]
b = a * data["eclairs"]
result = round(b)
print(result)