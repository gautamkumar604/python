class Calculator:
    def __init__(self,a):
        self.a = a
    def square(self):
        return f"The square of {self.a} is {self.a ** 2}"
    def cube(self):
        return f"The cube of {self.a} is {self.a ** 3}"
    def square_root(self):
        return f"The square_root of {self.a} is {self.a ** (1/2)}"

m = Calculator(8)
print(m.a)
print(m.square())
print(m.cube())
print(m.square_root())