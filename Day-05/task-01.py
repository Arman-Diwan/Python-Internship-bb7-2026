class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("My car is", self.brand, self.model, "and its year is", self.year)


car1 = Car("Toyota", "Fortuner", 2022)
car2 = Car("Honda", "City", 2021)
car3 = Car("BMW", "X5", 2023)

car1.display_info()
car2.display_info()
car3.display_info()