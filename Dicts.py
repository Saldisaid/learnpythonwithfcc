# pizza = {
#     'name': 'Pepperoni',
#     'price': 12.99,
#     'calories': 300,
#     'toppings': ['pepperoni', 'cheese', 'tomato sauce']
# }

# print(pizza['price'])
# pizza['name'] = 'Veggie Delight'
# print(pizza['name'])

# print(pizza.get('toppings', []))
# print(pizza['toppings'])
# print(pizza.keys())
# print(pizza.values())
# print(pizza.items())
# print(pizza.update({'calories': 250, 'size': 'Large'}))
# # print(pizza.items)
# print(pizza['size'])

products = {
    'Laptop': 999.99,
    'Smartphone': 499.99,
    'Tablet': 299.99,
    'Headphones': 199.99
}

for price in products.values():
    print(f"Price: ${price}")

for product in products.keys():
    print(f"Product: {product}")

for product, price in products.items():
    print(f"{product}: ${price}")

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

for index, product in enumerate(products, start=1):
    print(f"{index}. {product} - {products[product]}")

for index, values in enumerate(products.values(), start=1):
    print(f"{index}. Price - {values}")

for idx, products in enumerate(products.items(), start=1):
    print(f"{idx}. {products}")













