import random


robotmove = "testing"
robocount = 0
playercount = 0

for i in range(1):
    randomNum = random.random()
    print(randomNum)

if randomNum < 0.34:
    robotmove = "rock"
elif 0.34 <= randomNum <= 0.67:
    robotmove = "paper"
else:
    robotmove = "scissor"
#print(robotmove)

def rock_game():
    playerChoice = input("rock,paper, or scissor?")
    if playerChoice == "rock" and robotmove == "rock":
        print("Tie")
        rock_game()
        finalresult()
    elif playerChoice == "rock" and robotmove == "paper":
        print("You lose!")
        robocount =+1
        rock_game()
        finalresult()
    elif playerChoice == "rock" and robotmove == "scissor":
        print("You win!")
        playercount =+1
        rock_game()
        finalresult()
    elif playerChoice == "paper" and robotmove == "rock":
        print("You win!")
        playercount =+1
        rock_game()
        finalresult()
    elif playerChoice == "paper" and robotmove == "paper":
        print("Tie")
        rock_game()
        finalresult()
    elif playerChoice == "paper" and robotmove == "scissor":
        print("You lose!")
        robocount =+1
        rock_game()
        finalresult()
    elif playerChoice == "scissor" and robotmove == "scissor":
        print("Tie")
        rock_game()
        finalresult()
    elif playerChoice == "scissor" and robotmove == "paper":
        print("You win!")
        playercount =+1
        rock_game()
        finalresult()
    elif playerChoice == "scissor" and robotmove == "rock":
        print("You lose!")
        robocount =+1
        rock_game()
        finalresult()
rock_game()

def finalresult():
    if playercount == 5:
        print("Final victory is yours")
    elif robocount == 5:
        print("You lost to a random number generator, sad!")
