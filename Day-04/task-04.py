usernames = ["arman", "rahul", "alex", "hassan", "john123", "diwan"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print("Original Usernames:", usernames)
print("Filtered Usernames:", result)