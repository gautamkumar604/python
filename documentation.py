# this is my python notebook

'''
list--> A built in data type that lets us create mutable sequence of values
Syntax--> list name = [comma seprated values]
ex--> list = [1,5,2,3]

# list = [5,4,2,3,1]
# print(list)
# list.append(15)
# list.sort()
# list.insert(2,6)
# list.sort(reverse=True)
# list.remove(4)
# list.pop(4)
# print(type(list))


tuples--> A built in data type that lets us create immutable sequence of values
Syntax--> tuple name = (comma seprated values)
ex--> tup = (1,5,2,3)
tup =("gautam","Hello","Nature","Young","Hello")
print(type(tup))
print(tup)
print(tup.count("Hello"))#return the number repeat Element


Dictionary-->Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable(Mutable) and do not allow duplicates.
Syntax-->   dict = {
                key : value,
                key: value
            }

Example-->
            dict = {
                "name" : "Gautam Kumar",
                "age" : 21,
                "gender" : "Male"
            }
            print(type(dict))
            print(dict)
            print(dict["name"])
            dict["age"]=25 #Change the value of age
            dict["Mobile no"]=9304157406
            dict.clear()
            print(dict.get("age"))
            print(dict)



set-->Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Syntax-->   myset = {a1,a2,a3 (#comma seprated values)}
            myset = {4,2,3,5,6}
            myset2 = {1,9,3,8,6}
            print(type(myset))
            myset.add(25)
            # myset[2]=23 #can't support item assignment
            print(myset.intersection(myset2))
            print(myset)


Loops--------------------------------
loops is a block of code to execute for repitedly works according to given conditions
-->Basically two type of loops in python programming language
1. while Loop --> Syntax-   while(conditions):
                                 #Code
                                 #Condition increment 
                            #End

                  Example-  count = 1
                            while(count<=5):
                                print("Hello | World")
                                count+=1

                            print("end")

2. for Loop --> Syntax-    for element in variable_Name:
                                 #Code
                                 
                            #End

                Example-    list = ["Hello","Welcome","Somthing","Smart"]
                            for el in list:
                                print(el, end=" ")

*  for Loop --> Syntax-     for element in range(start-point,end-point):
                                 #Code
                                 
                            #End

                Example-    n = int(input("Enter number for create table up to 10: "))
                            for el in range(1,11):
                                print(n,"*",el," = ", n*el)




                                
Functions--> A function is a block of code which only runs when it is called.
             You can pass data, known as parameters, into a function.
             A function can return data as a result.

         --> In Python a function is defined using the def keyword: 
         --> Basically functions are two types in python 
             1. Built in Functions
                as- print(),len(),input(), etc
             1. User define(def) Functions
                as- created by programmer
                
Syntax-->   def Function_Name(parameter):
                #code here
            #End
                
Example-->  def my_function(fname):
                print(fname + " Refsnes")

            my_function("Emil")
            my_function("Tobias")
            my_function("Linus")

Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

'''
