def create_frozenset(mylist):
    return frozenset(mylist)


numbers = [10, 20, 30, 40, 20, 10]

result = create_frozenset(numbers)

print("Original List:", numbers)
print("Frozenset:", result)