
grocery_prices = {
    "Milk": 50,
    "Bread": 30,
    "Eggs": 60,
    "Rice": 80,
    "Sugar": 40
}

grocery_quantity = {
    "Milk": 3,
    "Bread": 2,
    "Eggs": 6,
    "Rice": 3,
    "Sugar": 2
}

total_bill = sum(grocery_prices[item] * grocery_quantity.get(item, 0) for item in grocery_prices)

print("Total Bill:", total_bill)


