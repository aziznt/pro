import json

with open('orders.json', encoding="utf-8") as f:
    orders = json.load(f)

for order in orders:
    customer = order['customer_name']
    items = order['items']
    total = sum([item['price']*item['quantity'] for item in items])
    print(f"{customer}: ${total}")
print("HEllo github")
