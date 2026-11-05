numbers = [10, 25, 45, 80, 60, 90, 35]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest Number:", largest)
print("Second Largest Number:", second_largest)