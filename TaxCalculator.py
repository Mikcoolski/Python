#This is a simple tax calculator and display prompt
amount = 3428 
tax = .07
total = amount*tax
promptMessage = "The tax rate is {} and for your purchase order of {} comes out to a total tax of {}"
print(promptMessage.format(tax,amount,total))
