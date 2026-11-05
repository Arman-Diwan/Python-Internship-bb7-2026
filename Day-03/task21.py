employees = {
    "Rahul": 25000,
    "Aman": 50000,
    "Riya": 40000,
    "Sara": 60000,
    "Neha": 35000
}

# Sorting by salary in descending order
sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Highest Paid Employees:")

for name, salary in sorted_employees[:3]:
    print(name, ":", salary)