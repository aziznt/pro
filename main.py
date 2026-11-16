import json

with open('orders.json', encoding="utf-8") as f:
    orders = json.load(f)
print(orders)