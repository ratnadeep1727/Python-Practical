# Demonstrating Method Overloading
# Method Overloading in python doesn't support

class OverloadingDemo:
    def add(self, a=None, b=None, c=None):
        """Demonstrates method overloading by handling variable arguments."""
        if a != None and b != None and c != None:
            print(a + b + c)
        elif a != None and b != None:
            print(a + b)
        elif a != None:
            print(a)
        else:
            print("empty")
        
obj = OverloadingDemo()
obj.add(2,3,4)
obj.add(2,3)
obj.add(2)
obj.add()

print()

# Demonstrating Method Overriding
class Parent:
    def display_message(self):
        print("This is a message from the Parent class.")

class Child(Parent):
    def display_message(self):
        print("This is a message from the Child class (overriding Parent's method).")

parent = Parent()
parent.display_message()  # Call the parent class method

child = Child()
child.display_message()  # Call the overridden method in the child class
