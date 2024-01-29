# finding the largest number from the lists 
                                    # 1

numbers = [1,2,3,4,5,6,7,8,9,32,55,44,22,55,44,33]
numbers.sort()     
print(" number is the largest",numbers[-1])

                                        # 2
numbers = [1,2,3,4,5,6,7,8,9,32,55,44,22,55,44,33]
print("largest number is",max(numbers))

                                         # 3
numbers = [1,2,3,4,5,6,7,88,66,99,44]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)        

lists = [1,2,3,4,5]               
print(lists)                        

lists = ['maaz','saad','haris']     
print(lists)     

lists[1] = 'khan' # replacement
print(lists)

lists = [1,2,3,4,5,6,7]
print(lists[3:])

lists = [1,2,3,4,5,6,7]
print(lists[:])    #by default it prints all the element

lists = [1,2,3,4,5,'maaz',7]
print("index [5] \n",lists[5])
