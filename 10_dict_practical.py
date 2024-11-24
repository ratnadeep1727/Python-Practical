# Create Dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Access Dictionary elements
print("Accessing elements:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict.get('city'))  # Using get() to access element

# Update Dictionary
print("\nUpdating Dictionary:")
my_dict['age'] = 26  # Updating value
my_dict['country'] = 'USA'  # Adding new key-value pair
print("Updated Dictionary:", my_dict)

# Delete Dictionary
print("\nDeleting a key from Dictionary:")
del my_dict['city']  # Deleting key 'city'
print("Dictionary after deletion:", my_dict)

# Looping through Dictionary
print("\nLooping through Dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)
