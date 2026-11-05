class Counter:
    count = 0

    def __init__(self):
        Counter.count = Counter.count + 1

    @classmethod
    def get_count(cls):
        return cls.count


c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total objects created:", Counter.get_count())