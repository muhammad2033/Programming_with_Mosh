import random

for i in range(3):
    print(random.random())


for i in range(4):
    print(random.randint(11,18))    #will give us 4 random values or digits

lists = ['maaz','khan','khalil','saad','python']  #will print the random names from the lists
print(random.choice(lists))    


import random
class dice:
    def dices (self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first,second)

maaz= dice()
maaz.dices()
print("rolling for maaz\n")
print(maaz.dices())



saad= dice()
saad.dices()
print("rolling for saad\n")

print(saad.dices())


