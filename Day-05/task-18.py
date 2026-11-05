class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
        print(item, "added to stack")

    def pop(self):
        if len(self.__items) == 0:
            print("Stack is empty")
        else:
            return self.__items.pop()

    def __str__(self):
        return str(self.__items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Current Stack:", s)

print("Removed Item:", s.pop())

print("Updated Stack:", s)