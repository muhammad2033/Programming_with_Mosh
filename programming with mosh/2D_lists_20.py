matrix = [ 

        [1,2,3],
        [4,5,6],
        [7,8,9]    


]
matrix [2][2] = 99  # replacement
matrix [1][2] = 88
matrix [0][2] = 77
matrix [2][0] = 66
print(matrix)

print("wanna excess the 1 \n",matrix[0][0])
print("wanna excess the 88 \n",matrix[1][2])
print("wanna excess the 7 \n",matrix[2][0])

for row in matrix:
    for item in row:
        print(item)      # all the matrix element will print in a column
