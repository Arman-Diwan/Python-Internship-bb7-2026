class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary increased successfully")
        else:
            print("Error: Salary cannot be decreased")


e1 = Employee(20000)

print("Current Salary:", e1.get_salary())

e1.set_salary(30000)
print("Updated Salary:", e1.get_salary())

e1.set_salary(15000)
print("Final Salary:", e1.get_salary())