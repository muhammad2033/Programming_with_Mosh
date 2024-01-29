# if within if is called nested if 

for x in range(2): 
    for y in range(2): 
        for z in range(2): 
            print(f"({x},{y}) ")

            #challenge

numbers = ['xxxxx','xx','xxxxx','xx','xx']
     
for x in numbers:
        print( x)             

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)                

numbers = [2,2,2,5]
for x_count in numbers:
    output = '\t'
    for count in range(x_count):
        output += 'x'
    print(output) 

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = '\t'
    for count in range(x_count):
        output += 'x'
    print(output)    
    
numbers = [6,6,6,2,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)                                               