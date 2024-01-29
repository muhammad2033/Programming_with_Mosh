

lists = [1,2,3,4,5,6,7]
lists.append(8)     #add an element at the end
print(lists)

lists = [1,2,3,4,5,6,7,8]
lists.pop()     # delete an element from the end 
print(lists)

lists = [1,2,3,4,5,6,7]   #used to clarify all the element
lists.clear()
print(lists)

lists = [1,2,3,4,5,6,7]
lists.insert(2,6)  #index [2], we added a 6 digit, used to add an element anywhere in list
print(lists)

lists = [1,2,3,4,5,6,7]
lists.remove(4)  # used remove the exect element ,like 4
print(lists)

lists = [1,2,3,4,5,6,7]
print(lists.index(5))  # finding the index of the element 
print(lists.index(7))  #7 is located at index 6
# print(lists.index(44)) # error will get,44 is not in the list

print(44 in lists)  # spare us booleon value,false
print(6 in lists)  # spare us booleon value,true

lists = [1,2,3,3,3,3,3,3,4,5,3,3,3,3,6,3,3,3,3,7,5,5,5,5,5,5,5,5,5,5]
print(lists.count(3))  # use to count the repeated element in a list
print(lists.count(5))  # use to count the repeated element in a list
print(lists.count(6))  # use to count the repeated element in a list


lists = [1,2,3,4,7,8,9,55,6,8,99]
lists.sort()
print(lists) #use to sort the list

lists = [1,2,3,4,7,8,9,55,6,8,99]
lists.reverse()
print(lists) #use to reverse the list

lists = [1,2,3,4,7,3,4,8,9,55,6,8,99]
uniqu = []
for number in lists: 
    if number not in uniqu:
        uniqu.append(number) 
print(uniqu)
                                #COPY()
lists = [1,2,3,4,7,3,4,8,9,55,6,8,99] 
number2 = lists.copy()
lists.append(11)    # doesnt append coz they are independent lists
print(number2)





