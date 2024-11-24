# 1. Create a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Created Tuple:", my_tuple)

# 2. Access Tuple Elements
print("Access first element:", my_tuple[0])  # Access by index
print("Access last element:", my_tuple[-1])  # Access by negative index
print("Access a slice (first 3 elements):", my_tuple[:3])  # Slicing

# 3. Update a Tuple (Tuples are immutable, so we create a new one)
new_tuple = my_tuple + (60, 70)  # Adding elements to a tuple
print("Updated Tuple after adding elements:", new_tuple)

# To remove an element, convert to a list (not direct operation on tuple)
temp_list = list(new_tuple)
temp_list.remove(30)  # Removing an element
updated_tuple = tuple(temp_list)
print("Updated Tuple after removing an element:", updated_tuple)

# 4. Delete the Tuple
del updated_tuple  # Deletes the tuple
# Trying to access it now will cause an error
try:
    print("Trying to access deleted tuple:", updated_tuple)
except NameError:
    print("The tuple has been deleted and no longer exists.")


# # Create a Tuple
# my_tuple = (10, 20, 30, 40, 50, 10)

# # 1. Count the occurrences of an item
# count_of_10 = my_tuple.count(10)
# print("Count of 10:", count_of_10)

# # 2. Find the index of an item
# index_of_30 = my_tuple.index(30)
# print("Index of 30:", index_of_30)

# # 3. Length of the Tuple
# length_of_tuple = len(my_tuple)
# print("Length of tuple:", length_of_tuple)

# # 4. Concatenate Tuples
# another_tuple = (60, 70, 80)
# concatenated_tuple = my_tuple + another_tuple
# print("Concatenated Tuple:", concatenated_tuple)

# # 5. Repeat a Tuple
# repeated_tuple = my_tuple * 2
# print("Repeated Tuple:", repeated_tuple)

# # 6. Slice a Tuple
# sliced_tuple = my_tuple[1:4]  # Elements from index 1 to 3
# print("Sliced Tuple:", sliced_tuple)

# # 7. Check if an item exists in a Tuple
# is_40_in_tuple = 40 in my_tuple
# print("Is 40 in the tuple?", is_40_in_tuple)

# # 8. Iterate through a Tuple
# print("Iterating through the tuple:")
# for item in my_tuple:
#     print(item)
