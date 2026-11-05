def access_list(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print("Error: Index does not exist")
        return None


numbers = [10, 20, 30, 40]

print(access_list(numbers, 2))
print(access_list(numbers, 10))