class Employee:
    def calculate_salary(self):
        return 20000


class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 10000


class Designer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 5000


e1 = Developer()
e2 = Designer()

print("Developer Salary:", e1.calculate_salary())
print("Designer Salary:", e2.calculate_salary())