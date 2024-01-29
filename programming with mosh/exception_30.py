# from __future__ import division


try:
    name = "maaz"
    print(maaz)

except NameError:
    print("invalid name....")
    print("how are you ")

try:
    age = 22
    day = 0
    division = age/day
    print(division)   

except ZeroDivisionError:
    print("age", age)   
    print("invalid ZeroDivisionError")





    # similarly exceptions work  