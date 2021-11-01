Temperature = float(input("What is the temperature outside?:\n"))

if(Temperature >=80):
    if (Temperature>100):
        print("Its Sweltering")
    else: 
        print("Its Too Hot")
else:
    if Temperature<80 and Temperature>=65:
        print("Its Perfect!")
    else: print("Its getting cold")

 