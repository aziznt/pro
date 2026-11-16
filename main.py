import json

with open('orders.json', encoding="utf-8") as f:
    orders = json.load(f)

exps = {}

for order in orders:
    customer = order['customer_name']
    items = order['items']
    total = sum([item['price']*item['quantity'] for item in items])
    exps[customer] = total
    print(f"{customer}: ${total}")

rich = max(exps, key=exps.get)
amount = exps[rich]
print(f"{rich} ${amount}")

