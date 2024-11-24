# 1. Create a List
my_list = [10, 20, 30, 40, 50]
print("Created List:", my_list)

# 2. Access Elements in the List
print("Access first element:", my_list[0])  # Access by index
print("Access last element:", my_list[-1])  # Access by negative index

# 3. Update the List
# Add an item
my_list.append(60)  # Adds 60 to the end
print("List after adding an item (60):", my_list)

# Remove an item
my_list.remove(30)  # Removes the first occurrence of 30
print("List after removing an item (30):", my_list)

# 4. Delete the List
del my_list  # Deletes the entire list
# Trying to access it now will cause an error
try:
    print("Trying to access deleted list:", my_list)
except NameError:
    print("The list has been deleted and no longer exists.")

# # Create a sample list
# my_list = [10, 20, 30, 40, 50]

# # 1. Append an item
# my_list.append(60)
# print("After append:", my_list)

# # 2. Extend the list with another list
# my_list.extend([70, 80])
# print("After extend:", my_list)

# # 3. Insert an item at a specific index
# my_list.insert(2, 25)  # Insert 25 at index 2
# print("After insert:", my_list)

# # 4. Remove an item
# my_list.remove(30)  # Removes the first occurrence of 30
# print("After remove:", my_list)

# # 5. Pop an item (removes and returns the last item by default)
# popped_item = my_list.pop()
# print("After pop:", my_list)
# print("Popped item:", popped_item)

# # 6. Index of an item
# index_of_40 = my_list.index(40)  # Finds the index of 40
# print("Index of 40:", index_of_40)

# # 7. Count occurrences of an item
# count_of_20 = my_list.count(20)  # Counts how many times 20 appears
# print("Count of 20:", count_of_20)

# # 8. Sort the list
# my_list.sort()
# print("After sort (ascending):", my_list)

# # 9. Reverse the list
# my_list.reverse()
# print("After reverse:", my_list)

# # 10. Copy the list
# copied_list = my_list.copy()
# print("Copied list:", copied_list)

# # 11. Clear the list
# my_list.clear()
# print("After clear:", my_list)
