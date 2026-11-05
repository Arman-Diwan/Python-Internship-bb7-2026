tasks = []

# Adding 5 tasks
tasks.append("Complete Python Assignment")
tasks.append("Study DBMS")
tasks.append("Practice Java")
tasks.append("Learn HTML and CSS")
tasks.append("Complete Project")

print("All Tasks:")
for task in tasks:
    print(task)

# Removing 2 tasks
tasks.remove("Study DBMS")
tasks.remove("Practice Java")

print("\nTasks After Removing 2 Tasks:")
for task in tasks:
    print(task)