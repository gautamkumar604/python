class Employee: #Base class(Parent class)
    a = 4
    def __init__(self):
        print("This is Employee class constructor")

class Coder: #this is another Base class
    b = 5
    def __init__(self):
        print("This is Coder class constructor")

class Programmer(Employee,Coder):#Derived class(child class) inharited from Base class Employee and Coder
    c = 10
    def __init__(self):
        # super().__init__() # use super key to call base class methods
        print("This is Programmer class constructor")

    def add(self):
        print(f"a + b + c = {self.a + self.b + self.c}")

obj = Programmer()
obj.add()