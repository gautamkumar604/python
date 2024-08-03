class Employee:

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.name = "kaliya Bhai"
print(e.fname)
print(e.lname)
# print(e.name)