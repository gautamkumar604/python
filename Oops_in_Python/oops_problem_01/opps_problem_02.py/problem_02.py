class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):

    def bark(self):
        print("Bow Bow Bow...")

obj = Dog()
obj.bark()