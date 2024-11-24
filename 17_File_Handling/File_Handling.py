# Opening file in different modes
# Opening file in write mode (w) and writing content
# 'w' mode creates a new file or overwrites the existing file.
f = open("text.txt", "w")
data = f.write("I'm learning a Python language.")
print(f"Number of characters written: {data}")
f.close()

# Opening file in read mode (r) and reading content
# 'r' mode opens an existing file for reading.
f = open("text.txt", "r")
data = f.read()
print(f"Content of the file: {data}")
f.close()

# Opening file in append mode (a) and appending content
# 'a' mode appends content at the end of the file.
f = open("text.txt", "a")
data = f.write("\nNow, I'm attending my Python practical.")
print(f"Number of characters appended: {data}")
f.close()

# Opening file in read/write mode (w+) and writing content
# 'w+' mode creates the file or overwrites the file and allows both reading and writing.
f = open("text.txt", "w+")
data = f.write("I'm learning a Python language.")
print(f"Number of characters written: {data}")
f.close()

# Opening file in read/write mode (r+) and reading content
# 'r+' mode allows both reading and writing on an existing file.
f = open("text.txt", "r+")
data = f.read()
print(f"Content of the file: {data}")
f.close()

# Opening file in append/read mode (a+) and appending content
# 'a+' mode allows both appending and reading the content of the file.
f = open("text.txt", "a+")
data = f.write("\nNow, I'm attending my Python practical.")
print(f"Number of characters appended: {data}")
f.close()



# Accessing File

# Create and write to the file
f = open("text.txt", "w")
f.write("This is a demonstration of accessing files in Python.\n")
f.write("We can perform read, write, and append operations on files.\n")
f.close()

# Read the entire file content
print("\nReading the file content:")
f = open("text.txt", "r")
content = f.read()
print(content)
f.close()

# Read the file line by line
print("\nReading the file line by line:")
f = open("text.txt", "r")
for line in f:
    print(line.strip())
f.close()

# Append new content to the file
print("\nAppending new content to the file.")
f = open("text.txt", "a")
f.write("Appending more text to the file.\n")
f.close()

# Verify the appended content
print("\nContent after appending:")
f = open("text.txt", "r")
print(f.read())
f.close()



# Closing File 
f.close()



# Renaming and Deleting File 
import os

#  os.rename("text.txt", "text1.txt") #rename the file 
#  os.remove("text1.txt") # delete the file 