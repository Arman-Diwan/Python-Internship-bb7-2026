library = {
    101: {"title": "Python", "author": "John", "copies": 5},
    102: {"title": "Java", "author": "James", "copies": 3},
    103: {"title": "C++", "author": "Bjarne", "copies": 4}
}

# Issuing book with ID 101
book_id = 101

library[book_id]["copies"] -= 1

print("Updated Library:")
print(library)