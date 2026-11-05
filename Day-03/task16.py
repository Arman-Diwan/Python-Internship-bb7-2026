products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 800,
    "Pen": 20,
    "Monitor": 12000
}

new_products = {name: price for name, price in products.items() if price > 100}

print("Original Dictionary:", products)
print("Products Above 100:", new_products)