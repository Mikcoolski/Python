#Creating first python function here

def greeting(name):
    print("Hi how are you",name)

def farewell(name1,name2):
    print("Take care", name1,",",name2)

#Main program which will use the function created
inputFirstName = input("Enter your name to be greeted by th python program:")
inputLastName = input("What is your last name though?")

greeting(inputFirstName)
farewell(inputFirstName,inputLastName)