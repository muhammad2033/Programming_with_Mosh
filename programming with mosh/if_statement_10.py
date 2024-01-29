from turtle import down


name = True
name2 = True   #it is a python interpreter , so it executes the program line by line
if name:        # so the first statement will execute if both are true
    print("hy!")
    print("maaz")
    print("have a great day ahead!")    
elif name2:
    print("name2 must be executed if true")
    print("if no , then the else statement will execute ")

else:
    print("maaz is here")
    print("i dont know")
print("have A nice day")    

                            # # EXAMPLE
                            # price of a house is 1m dollar
                            # if a buyer has a good credit,
                            #     they need to put down 10%
                            # otherwise
                            #     they need to put down 20%
                            # print the down payment     

price = 1000000
has_good_credit = False 

if has_good_credit:
    down_payment =0.1*price

else:                   
    down_payment = 0.2 * price

print(f"down_payment is....{down_payment} dollars")                 
     