def calculate_sum(n):
    if n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)


number = 5

result = calculate_sum(number)

print("Sum of numbers from 1 to", number, "is:", result)