#Fun with lists in python

#create a pre-defined list
newList = ["first","second","third","fourth"]

#Display the pre-defined list
displayList = "The contents within the pre-defined list is {}"
print(displayList.format(newList))

#User input list
print("Enter in 10 different values:\n")

#initialize the list
userList = []

#loop 10 times starting at 0 for inputs
for i in range(0,10):
    userList.append(input("Enter a value:"))

#display the user defined list
print("Here is your defined list of values")
for value in userList:
    print(value)