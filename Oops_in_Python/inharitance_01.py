class Employee: #Base class(Parent class)
    def __init__(self):
        print("This is Employee class constructor")

class Programmer(Employee):#Derived class(child class) inharited from base class
    def __init__(self):
        # super().__init__() # use super key to call base class methods
        print("This is Programmer class constructor")

obj = Programmer()