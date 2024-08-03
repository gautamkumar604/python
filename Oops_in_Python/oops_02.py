class Employee:
    company = "Microsoft"  #class Attributes
    branch = "data Scientist"
    sallery = 120000
    
# gautam = Employee()
# print(f"company: {gautam.company}\nbranch: {gautam.branch}\nsallery: {gautam.sallery}")

gautam = Employee()
#instance(object) Attribute has more preference than class attribute in python)
gautam.sallery = 150000 #instance(object) Attribute (Preference)
print(f"company: {gautam.company}\nbranch: {gautam.branch}\nsallery: {gautam.sallery}")
        