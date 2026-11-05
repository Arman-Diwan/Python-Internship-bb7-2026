def outer_function():
    status = "pending"

    def inner_function():
        nonlocal status
        status = "completed"

    inner_function()

    print("Final Status:", status)


outer_function()