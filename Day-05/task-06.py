class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height


r1 = Rectangle(10, 5)
r2 = Rectangle(20, 2.5)

if r1 == r2:
    print("Both rectangles are equal")
else:
    print("Rectangles are not equal")