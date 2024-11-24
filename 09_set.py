# 1. Create a Set
my_set = {10, 20, 30, 40, 50}
print("Created Set:", my_set)

# 2. Access Set elements (Sets are unordered, so access is done differently)
# We can iterate over the set to access elements
print("Accessing elements in the set:")
for element in my_set:
    print(element)

# 3. Update a Set (Adding and Removing elements)
# Add an item
my_set.add(60)
print("Set after adding an item (60):", my_set)

# Add multiple items (using update)
my_set.update([70, 80])
print("Set after adding multiple items (70, 80):", my_set)

# Remove an item
my_set.remove(30)  # Removes 30 from the set
print("Set after removing item (30):", my_set)

# If the item doesn't exist and we use remove, it raises a KeyError.
# To avoid this, we can use discard (it won't raise an error if the item is not found)
my_set.discard(100)  # Item 100 is not in the set, no error will be raised
print("Set after discard (100, which is not present):", my_set)

# 4. Delete a Set
del my_set  # Deletes the entire set
# Trying to access it now will cause an error
try:
    print("Trying to access deleted set:", my_set)
except NameError:
    print("The set has been deleted and no longer exists.")

