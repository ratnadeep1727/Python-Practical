# Demonstrating 'continue'
print("Using 'continue':")
for i in range(1, 6):
    if i == 3:
        continue  # Skips the rest of the loop for i = 3
    print(f"i = {i}")
print()

# Demonstrating 'pass'
print("Using 'pass':")
for i in range(1, 6):
    if i == 3:
        pass  # Does nothing, just a placeholder
    print(f"i = {i}")
print()

# Demonstrating 'break'
print("Using 'break':")
for i in range(1, 6):
    if i == 3:
        break  # Exits the loop when i = 3
    print(f"i = {i}")
