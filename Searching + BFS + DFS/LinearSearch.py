'''
Linear search is a simple algorithm that:
	•	Checks each element of a list one by one, starting from the first.
	•	Compares every element to the target value.
	•	Returns the index (position) when a match is found.
	•	Returns -1 or indicates “not found” if the end is reached without a match

Linear Search in Practice
	•	Simple to understand and code; good for small lists.
	•	Time complexity:  where  is the length of the list.
	•	Not efficient for large or sorted lists (Binary Search is better if sorted).
	•	Python `in` operator, `.index()` method, and simple loops all perform linear searches under the hood
'''

beasts = ["Centaur", "Godzilla", "Mosura", "Minotaur", "Hydra", "Nessie"]

# Find index of "Godzilla". Uses Linear Search under the hood.
index_godzilla = beasts.index("Godzilla")  # Returns the index or raises ValueError

# Find index using a function (like findIndex)
def find_index(list, target):
    for i, item in enumerate(list):
        if item == target:
            return i
    return -1

index_godzilla2 = find_index(beasts, "Godzilla")

# Find the actual item (like find)
def find_item(list, target):
    for item in list:
        if item == target:
            return item
    return None

found_godzilla = find_item(beasts, "Godzilla")

# Check if "Godzilla" is in the list (like includes). Again Linear search.
is_godzilla_present = "Godzilla" in beasts
