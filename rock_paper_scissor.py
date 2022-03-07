
import random
computer = random.randrange(1,3,1)
user = int(input("Enter number from 1 to 3 as Rock, Paper Scissor respectively."))
print("Computer choose :",computer)
if computer== user :
    print("Tie")
elif computer ==1 and user ==2:
    print("User - paper won against rock -computer")
elif computer == 1 and user == 3:
    print("Computer-rock won against scissors-User")
elif computer == 2 and user == 1:
    print("Computer-paper won against rock-User")
elif computer == 2 and user == 3:
    print("User-scissors won against computer-paper")
elif computer == 3 and user == 1:
    print("User - rock won against scissors-Computer")
elif computer == 3 and user == 2:
    print("Computer-scissor won against User-paper")