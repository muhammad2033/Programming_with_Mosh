                                            #    method 1             

n =int(input("input the number for factorial..."))

product = 1
for i in range(n):
    product = product*(i+1)
print(product)

                                            # method 2

n = 4
product = 1
for i in range(n):
    product = product* (i+1)
print(product)


                                            #method 3
def factorial(n):
    product = 1
    for i in range(n):                                                 
        product = product * ( i +1 )

    return product 
value = factorial(6)    #anything can be here       
print(value)

                                            #METHOD 4


def factorial(n):
    product = 1
    if n== 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1) 

print(factorial(1) )                                                      