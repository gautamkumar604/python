'''
water for -1
snake for 0
gun for 1

'''
import random
randstr = random.randrange(-1 , 2)

you = input("Enter your choise in 'snake','water' and 'gun': ")
if(you == "water"):
    you = -1
    print("you are choose water")
elif(you=="snake"):
    you = 0
    print("you are choose snake")
else:
    you = 1
    print("you are choose gun")

computer = randstr
if(randstr==-1):
     print("computer choose water")
elif(randstr==0):
     print("computer choose snake")
else:
     print("computer choose gun")
if(computer == you):
    print("Match is Draw")

else:
    if(computer == -1 and you == 0):
        print("you are win the game|hurrrrrey")
    elif(computer == -1 and you == 1):
         print("you are loss the game")
    elif(computer == 0 and you == -1):
         print("you are loss the game")
    elif(computer == 0 and you == 1):
         print("you are win the game")
    elif(computer == 1 and you == -1):
         print("you are win the game")
    elif(computer == 1 and you == 0):
         print("you are loss the game")
    else:
         print("Please| Enter a valid character")


