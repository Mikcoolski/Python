#cool game in tutorial

#Usded to calculate a random number
import random

#Message to identify what the computer choice was
printmessage = "\nThe computer chose {}\n"

#define the computer choice
ComputerRandomChoice = random.choice(["Scissors","Rock","Paper"])

#define the user choice
UserChoice = input("What do you choose?\n")

#display the computer's choice]
print(printmessage.format(ComputerRandomChoice))

#compute the game logic and display the result
if UserChoice == ComputerRandomChoice:    
        print("The match is a tie\n")
elif UserChoice == "Scissors" and ComputerRandomChoice == "Paper":            
        print("You Win\n")
elif UserChoice == "Rock" and ComputerRandomChoice == "Scissors":            
        print("You Win\n")
elif UserChoice=="Paper" and ComputerRandomChoice == "Rock":    
        print("You Win\n")
else:    
        print("You lost\n")