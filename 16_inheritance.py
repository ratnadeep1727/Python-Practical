# Simple Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


#Multiple Inheritance
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    def bat_info(self):
        print("Bats are nocturnal and can use echolocation.")

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()
b1.bat_info()  # Custom method in the Bat class
