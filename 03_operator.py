#Arithmetic Operator

a = 2
b = 4
print("Addition       : "+str(a+b))
print("Subtraction    : "+str(a-b))
print("Multiplication : "+str(a*b))
print("Division       : "+str(a/b))
print("Floor Division : "+str(a//b))
print("Modulus        : "+str(a%b))
print("Exponentiation : "+str(a**b))

# Logical Operator

c = 4
d = 5

if c > 2 and d > 4:
    print("C is greater than 2 and d is less than 6")
else:
    print("C is not greater than 2 and d is not less than 6")

if c > 3 or d > 7:
    print("C is greater than 3 and d is less than 7")
else:
    print("C is not greater than 2 and d is not less than 7")

if not(c > 7 and d < 6):
    print("yes")
else:
    print("no")


# Bitwise operator

h = 10
k = 4

print("h & k : ",h & k)
print("h | k : ",h | k)
print("h ^ k : ",h ^ k)
print("~ k : ", ~ k)
print("h >> k : ",h >> k)
print("h << k : ",h << k)
