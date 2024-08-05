class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,v2):
        i = self.i + v2.i
        j = self.j + v2.j
        k = self.k + v2.k
        return Vector(i,j,k)

    def __mul__(self,v2):
        i = self.i * v2.i
        j = self.j * v2.j
        k = self.k * v2.k
        return Vector(i,j,k)

    def __str__(self):
        return f"new vector [{self.i}i,{self.j}j,{self.k}k]"
    
    def __str__(self):
        return f"new vector [{self.i}i,{self.j}j,{self.k}k]"
    

v1 = Vector(2,3,2)
v2 = Vector(4,3,2)
print(v1+v2,"after sum")
print(v1*v2,"after multiply")