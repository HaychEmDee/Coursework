# This program stores and calculates the stock values of items on a café menu.

menu = ["coffee", "tea", "cake", "biscuits"]

print(f"This café sells {menu}.")

stock = {menu[0]: 50,
         menu[1]: 50,
         menu[2]: 10,
         menu[3]: 20}

print(f"This is how much the café has in stock of each. {stock}")

price = {menu[0]: 2,
         menu[1]: 1.75,
         menu[2]: 5,
         menu[3]: 0.5}

print(f"This is how much one of each item costs in £. {price}")

stock_value = []

for i in menu:
    item_value = (stock[i] * price[i])
    stock_value.append(item_value)

print(f"The stock of each item is worth {stock_value} in £, respectively.")

total_value = sum(stock_value)
print(f"The total stock is worth £{total_value}0.")