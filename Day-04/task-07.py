import time

def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start, "seconds")

    return wrapper


@timer
def calculate():
    total = 0

    for i in range(1, 1000001):
        total = total + i

    print("Sum:", total)


calculate()