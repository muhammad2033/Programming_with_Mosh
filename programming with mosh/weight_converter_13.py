weight = int (input("input the weight for normal human \n "))
unit = input("l (bs) or kg ")
if unit == 'l':                                 #:0
    converted = weight * 0.45
    print(f' you are {converted} kilos  ')
else:    
    converted = weight / 0.45
    print(f"you are {converted} pounds ")