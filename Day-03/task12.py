subscribers = {
    "riya@gmail.com",
    "aman@gmail.com",
    "sara@gmail.com",
    "rahul@gmail.com"
}

customers = {
    "aman@gmail.com",
    "rahul@gmail.com",
    "neha@gmail.com",
    "karan@gmail.com"
}

# Subscribers who never made a purchase
not_purchased = subscribers - customers

# Customers who never subscribed
not_subscribed = customers - subscribers

print("Subscribers who never purchased:")
print(not_purchased)

print("\nCustomers who never subscribed:")
print(not_subscribed)