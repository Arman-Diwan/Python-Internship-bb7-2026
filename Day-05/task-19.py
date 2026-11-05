class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies must be the same")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies must be the same")
        return self.amount > other.amount


m1 = Money(500, "INR")
m2 = Money(1000, "INR")

print("Is m1 less than m2?", m1 < m2)
print("Is m1 greater than m2?", m1 > m2)