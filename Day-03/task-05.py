students = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

students.sort(key=lambda x: x[1], reverse=True)

print("Students Sorted by Marks:")
for student in students:
    print(student)