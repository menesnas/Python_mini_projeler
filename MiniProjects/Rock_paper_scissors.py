"""
import random 

greetings = " Welcome to the RPS game "
print(greetings.center(50,"*"))
user_score, pc_score = 0, 0
while True:
    ch = int(input("1)Rock\n2)Paper\n3)Scissors\nChoose one..."))   
    pc = random.randint(1,3)
    if (ch == 1):
        if (pc == 1):
            print("Computer's choice: Rock\nRock equal to rock. Scoreless!")
        elif (pc == 2):
            print("Computer's choice: Paper\nPaper wraps stone. You lose!")
            pc_score += 100
        elif (pc == 3):
            print("Computer's choice: Scissors\nRock breaks scissors. You win!")
            user_score += 100
    elif (ch == 2):
        if (pc == 1):
            print("Computer's choice: Rock\nPaper wraps stone. You win!")
            user_score += 100
            
        elif (pc == 2):
            print("Computer's choice: Paper\nPaper equal to paper. Scoreless!")
            
        elif (pc == 3):
            print("Computer's choice: Scissors\nScissors cuts paper. You lose!")
            pc_score += 100
    elif (ch == 3):
        if (pc == 1):
            print("Computer's choice: Rock\nRock breaks scissors. You lose!")
            pc_score += 100
            
        elif (pc == 2):
            print("Computer's choice: Paper\nScissors cuts paper. You win!")
            user_score += 100
            
        elif (pc == 3):
            print("Computer's choice: Scissors\nScissors equal to scissors. Scoreless!")
    else:
        break
print("User score : {} \nComputer score : {}".format(user_score,pc_score))
"""