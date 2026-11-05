# Creating a product tuple
product = ("Laptop", 50000, 2)

print("Original Product:", product)

# Trying to change the price
product[1] = 55000

# Creating a new tuple with updated price
updated_product = (product[0], 55000, product[2])

print("Updated Product:", updated_product)