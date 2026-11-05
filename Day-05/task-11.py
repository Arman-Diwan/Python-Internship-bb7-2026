class Bird:
    def fly(self):
        print("Bird is flying in the sky")


class Airplane:
    def fly(self):
        print("Airplane is flying in the air")


class Drone:
    def fly(self):
        print("Drone is flying using remote control")


def start_flying(obj):
    obj.fly()


b = Bird()
a = Airplane()
d = Drone()

start_flying(b)
start_flying(a)
start_flying(d)