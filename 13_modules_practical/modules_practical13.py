import platform
import keyword
import operator
from usermodule_practical13 import greeting 


print(platform.system())
print()
print("Keyword List : ",dir(keyword))
print()
print("Operator List : ",dir(operator))
print()

print("Addition : ", operator.add(2,3))
print("Subtraction : ", operator.sub(7,2))
print("Multiplication : ", operator.mul(2, 5))

def check_keyword(word):
    if keyword.iskeyword(word):
        print(f"{word} is a python keyword")
    else:
        print(f"{word} is not a python keyword")

x = input("Enter a keyword : ")
check_keyword(x)

greeting("Ratnadeep")
