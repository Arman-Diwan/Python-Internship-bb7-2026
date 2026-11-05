students = [
    {"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "Rahul", "marks": 90}
]

highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("Topper Name:", highest["name"])
print("Highest Marks:", highest["marks"])