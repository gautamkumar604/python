class Programmer:
    company = "Microsoft"
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def getInfo(self):
        print(f"Company: {self.company}\nname: {self.name}\nage:{self.age}\nsalary: {self.salary}")
    

rohan = Programmer("Rohan",22,40000)
rohan.getInfo()
