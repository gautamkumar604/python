class Demo:
    a = 4
    
o = Demo()
print(o.a) #print the class attribute becouse instance attribute is not present
o.a = 0 # set the instance attribute
print(o.a) #print the instance attribute becouse instance attribute is present
print(Demo.a)#print the class attribute becouse class attribute is not change