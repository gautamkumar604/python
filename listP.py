# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
'''# firts method
#create a empty list
movies = []
#Take inputs from the user
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
'''

'''# second method
#create a empty list
movies = []
#Take inputs from the user
mov = input("Enter 1st movie: ")
movies.append(mov)
mov = input("Enter 2nd movie: ")
movies.append(mov)
mov = input("Enter 3rd movie: ")
movies.append(mov)
print(movies)'''


'''# third method
#create a empty list
movies = []
#Take inputs from the user
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)'''


# WAP to check if a list contains a palindrome of elements.(Hint:use copy()method)
# [1,2,3,2,1]     [1,"abc","abc",1]

#create a list
list1 = [1,2,3,2,1]
list2 = [1,2,3,4,1]
copylist1 = list1.copy()
copylist2 = list2.copy()
copylist1.reverse()
copylist2.reverse()
if(list2 == copylist2):
    print("list values is a palindrome")
else:
    print("list is not a palindrome")