def require_positive(func):
    def wrapper(*args, **kwargs):

        for value in args:
            if value <= 0:
                print("Error: All numbers must be positive")
                return

        for value in kwargs.values():
            if value <= 0:
                print("Error: All numbers must be positive")
                return

        return func(*args, **kwargs)

    return wrapper


@require_positive
def divide(a, b):
    print("Result:", a / b)


divide(10, 2)
divide(-10, 2)
divide(10, 0)