inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

# Adding new stock
inventory["Laptop"] += 5

# Adding a new product
inventory["Monitor"] = 8

# Selling a product
product = "Mouse"
quantity = 3

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("Product Sold Successfully")
    else:
        print("Not Enough Stock")
else:
    print("Product Not Found")

# Display inventory
print("\nFinal Inventory:")

for product, quantity in inventory.items():
    print(product, ":", quantity)