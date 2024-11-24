a = 1

# while loop
while a < 10:
    print(a)
    a +=1

print()    

# for loop
for a in range(0,10):
    print(a)


# Nested while loop
a = 1
while a < 3:  # Outer loop
    print(f"Outer loop value of a: {a}")
    b = 1
    while b < 4:  # Inner loop
        print(f"  Inner loop value of b: {b}")
        b += 1
    a += 1

print()

# Nested for loop
for a in range(1, 3):  # Outer loop
    print(f"Outer loop value of a: {a}")
    for b in range(1, 4):  # Inner loop
        print(f"  Inner loop value of b: {b}")
