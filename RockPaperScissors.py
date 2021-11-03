#cool game in tutorial

#Usded to calculate a random number
import random

#Message to identify what the computer choice was
printmessage = "\nThe computer chose {}\n"

#define the computer choice
ComputerRandomChoice = random.randint(1,3)
if ComputerRandomChoice == 1:
    ComputerChoice = "Scissors"
if ComputerRandomChoice == 2:
    ComputerChoice = "Rock"
if ComputerRandomChoice == 3:
    ComputerChoice = "Paper"

#define the user choice
UserChoice = input("What do you choose?\n")

#display the computer's choice]
print(printmessage.format(ComputerChoice))

#compute the game logic and display the result
if UserChoice=="Scissors":
    if ComputerChoice == "Scissors":
        print("The match is a tie\n")
    elif ComputerChoice == "Rock":            
        print("You Lost\n")
    elif ComputerChoice == "Paper":            
        print("You Won\n")
elif UserChoice=="Rock":
    if ComputerChoice == "Scissors":
        print("You won\n")
    elif ComputerChoice == "Rock":            
        print("The match is a tie\n")
    elif ComputerChoice == "Paper":            
        print("You lost\n")
elif UserChoice=="Paper":
    if ComputerChoice == "Scissors":
        print("You lost\n")
    elif ComputerChoice == "Rock":            
        print("You won\n")
    elif ComputerChoice == "Paper":            
        print("The match is a tie\n")
