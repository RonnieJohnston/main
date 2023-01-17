#Ronnie Johnston
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
str_arr = []
final_str = " "
#First loop, take user input 5 times and append it to the string array
for i in range(5):
    user_input = input("Enter a word: ")
    user_input = str(user_input)
    str_arr.append(user_input)

#Second loop, loop through each string in string array and construct the final string using them
for string in str_arr:
    final_str += (string + " ")

print("One String: ", final_str)