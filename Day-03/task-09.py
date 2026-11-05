def marks_result(marks):
    lowest = marks[0]
    highest = marks[0]
    total = 0

    for mark in marks:
        if mark < lowest:
            lowest = mark

        if mark > highest:
            highest = mark

        total = total + mark

    average = total / len(marks)

    return (lowest, highest, average)


marks = [85, 90, 72, 95, 80]

# Calling function and unpacking tuple
low, high, avg = marks_result(marks)

print("Lowest Mark:", low)
print("Highest Mark:", high)
print("Average Mark:", avg)