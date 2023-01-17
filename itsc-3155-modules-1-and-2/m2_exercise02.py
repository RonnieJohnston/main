#Ronnie Johnston
lower_arr = []
upper_arr = []
user_input = input("Enter a string: ")

#Store string as array of chars
temp_arr = list(user_input)

#Loop through input array and check for uppercase and lowercase letters, adding them in order in their respective arrays
#https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
for char in temp_arr:
    if (char.islower()):
        lower_arr.append(char)
    elif (char.isupper()):
        upper_arr.append(char)

#Create output string by adding contents of lower array followed by upper array
output = ""
for char in lower_arr:
    output += char
for char in upper_arr:
    output += char

print("Result: ", output)