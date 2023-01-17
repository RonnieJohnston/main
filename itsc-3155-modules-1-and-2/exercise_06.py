#Ronnie Johnston
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
#Initialize array with 5 columns and 5 rows
arr = [[0 for i in range(5)] for j in range(5)]
#Get user input and store it, accounting for index shift
row = input("Enter a row num from 1 to 5: ")
row = int(row) - 1
column = input("Enter a column num from 1 to 5: ")
column = int(column) - 1

#Set selected position equal to 1
arr[row][column] = 1

#Output each row in sequence
for row in arr:
    print(row)