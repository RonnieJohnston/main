#Ronnie Johnston
#https://stackoverflow.com/questions/17483557/python-transforming-one-dimensional-array-into-two-dimensional-array
char_arr = []
final_arr = []
#Get user input and store the string
user_input = input("Enter a string: ")
user_input = str(user_input)

#Get raw characters and store in a list
char_arr = [i for i in user_input]
#Construct 2D array from 1D character list.
#This is done by appending each character in groups of 3 from start to finish across i / 3 rows, where i is the size of char_arr
final_arr = [char_arr[i:i+3] for i in range(0, len(char_arr), 3)]
print(final_arr)