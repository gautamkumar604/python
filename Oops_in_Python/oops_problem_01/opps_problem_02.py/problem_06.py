class Vector:
    def __init__(self,l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    

v1 = Vector([2,3,2])
v2 = Vector([4,3,2])
print(len(v1))