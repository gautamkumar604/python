# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    i = 4
    j = 6 
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Your 2D Vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"Your 3D Vector is {self.i}i + {self.j}j + {self.k}k")

obj = TwoDVector(8,5)
obj.show()
obj = ThreeDVector(4,5,8)
obj.show()