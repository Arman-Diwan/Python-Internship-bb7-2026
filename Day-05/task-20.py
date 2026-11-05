import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print("Time taken:", end - self.start, "seconds")


with Timer():
    total = 0

    for i in range(1, 1000001):
        total = total + i

    print("Sum:", total)