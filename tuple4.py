
food_items = [
    ("burger", 200),
    ("pizza", 600),
    ("taco", 350),
    ("frankie", 100),
    ("sandwich", 300),
    ("bomboloni", 500)
]
def get_price(item):
    return item[1]

food_items.sort(key=get_price, reverse=True)

print(food_items)
