class Employee: #Base class(Parent class)
    a = 4
    def __init__(self):
        print("This is Employee class constructor")

class Coder(Employee): #this is derived class inharited from base class
    b = 5
    def __init__(self):
        print("This is Coder class constructor")

    def add(self):
        print(f"a + b = {self.a + self.b}")

class Programmer(Coder):#This is another Derived class(child class) inharited from Coder class
    c = 10
    def __init__(self):
        # super().__init__() # use super key to call base class methods
        print("This is Programmer class constructor")

    def add(self):
        print(f"a + b + c = {self.a + self.b + self.c}")

obj = Programmer()
obj1 = Coder()
obj1.add()