# print("FUNCTIONS-->")

# # def sum_of_two_num(a,b):
# #     print(a,"+",b," = ",a+b)

# # sum_of_two_num(4,8)
# # sum_of_two_num(1,5)
# # sum_of_two_num(0,8)
# # sum_of_two_num(4,2)
# # sum_of_two_num(9,8) 

# value = int(input("Enter your number: "))
# def table(value):
#     for el in range(1,11):
#         print(value,"*",el," = ",value*el)

# table(value)

# def my_function(*kid): #refreces in form of tuple accepted from function call
#   print("His last name is " + kid[0])

# my_function("Tobias", "Refsnes")

# def my_function(**kid): # If the number of keyword arguments is unknown,So accepted refrences in form of dictionary,add a double ** before the parameter name:
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# Return Values
# To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
