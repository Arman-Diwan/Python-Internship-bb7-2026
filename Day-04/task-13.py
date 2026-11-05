mode = "Global Mode"

def outer_function():
    mode = "Enclosing Mode"

    def inner_function():
        mode = "Local Mode"
        print("Inner Function:", mode)

    inner_function()

    print("Outer Function:", mode)


outer_function()

print("Global:", mode)