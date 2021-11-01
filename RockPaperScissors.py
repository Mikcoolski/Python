#cool game

#define the computer choice
Computerchoice = "Scissors"

#define the user choice
UserChoice = input("What do you choose?\n")

#compute the game logic
if UserChoice=="Scissors":
    print("Tie")
elif UserChoice=="Rock":
    print("Win")
elif UserChoice=="Paper":
    print("Lose")