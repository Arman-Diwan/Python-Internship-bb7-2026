class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Error: Amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully")


w = Wallet(1000)

w.deposit(500)
w.withdraw(200)

print("Current Balance:", w.balance)