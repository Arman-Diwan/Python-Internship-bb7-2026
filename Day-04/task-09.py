count = 0

def my_function():
    global count
    count = count + 1
    print("Function called")

my_function()
my_function()
my_function()
my_function()

print("Total function calls:", count)