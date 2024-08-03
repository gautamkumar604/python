class Employee:
    company = "Microsoft"  #class Attributes
    branch = "data Scientist"
    sallery = 120000
    
    # def __init__(self): #create an constructer of this Employee class to call itself after create an object of this Employee class
    #    print("constructer 1 call")

    def __init__(self,name,age,language): #create an constructer with multiple attributes
       print("constructer 2 call")
       self.name = name
       self.age = age
       self.language = language

# gautam = Employee()
# print(f"company: {gautam.company}\nbranch: {gautam.branch}\nsallery: {gautam.sallery}")


gautam = Employee("gautam kumar",21,"python")
#instance(object) Attribute has more preference than class attribute in python)
gautam.sallery = 150000 #instance(object) Attribute (Preference)
print(f"company: {gautam.company}\nbranch: {gautam.branch}\nsallery: {gautam.sallery}")
print(f"name: {gautam.name}")
print(f"age: {gautam.age}")
print(f"language: {gautam.language}")
        