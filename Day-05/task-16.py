class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]


inventory = Inventory()

inventory.add_item("Laptop")
inventory.add_item("Mobile")
inventory.add_item("Keyboard")
inventory.add_item("Mouse")

print("Total Items:", len(inventory))
print("First Item:", inventory[0])
print("Second Item:", inventory[1])