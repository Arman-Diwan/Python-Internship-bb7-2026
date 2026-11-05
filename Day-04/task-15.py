def safe_division(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except TypeError:
        print("Error: Please enter numbers only")


print(safe_division(10, 2))
safe_division(10, 0)
safe_division(10, "abc")