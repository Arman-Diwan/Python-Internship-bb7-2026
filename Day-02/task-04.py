price = 45
quantity = 7
budget = 500

# Total cost of 7 notebooks
total_cost = price * quantity

# Maximum notebooks we can buy
notebooks = budget // price

# Money left after buying notebooks
remaining_money = budget % price

print("Total cost of 7 notebooks:", total_cost, "rupees")
print("Notebooks we can buy:", notebooks)
print("Remaining money:", remaining_money, "rupees")