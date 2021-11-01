#This is a simple tax calculator and display prompt

#Obtain the name of user
name = input("What is your name?\n")
#obtain the amount the user purchased the product for
amount = float(input("How much did you spend on your product?\n"))
#obtian the tax bracket the user was taxed at
tax = float(input("What is the tax bracket you were charged at?\n"))
#Calculate the total
total = float(amount*tax)
#Displayt he calculated tax price the user was charged 
promptMessage = "At the tax rate of  {} and for a purchase order amount of {}, the  total tax equates to {}"
print(promptMessage.format(tax,amount,total))
