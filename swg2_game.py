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
elif(you =="snake"):
    you = 0
    print("you are choose snake")
elif(you == "gun"):
    you = 1
    print("you are choose gun")
else:
     you = -3
     print("invalid value")

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
    if((computer - you) == -1 or (computer - you) == 2):
         print("you win")
    elif((computer - you) == 1 or (computer - you) == -2):
         print("you loss")
    else:
         print("????????????????????")


