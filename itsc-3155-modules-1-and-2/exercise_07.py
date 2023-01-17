#Ronnie Johnston
user_input = ''
total_arr = []
even_arr = []

#Keep taking input until QUIT is sent
while user_input != 'QUIT':
    user_input = input("Enter a number or QUIT to quit: ")
    #If user input is QUIT, exit while loop
    if user_input == 'QUIT':
        break
    user_input = int(user_input)
    #Add input to full array
    total_arr.append(user_input)
    #If input is divisible by 2, add it to even array
    if (user_input % 2 == 0):
        even_arr.append(user_input)

print("All nums: ", total_arr)
print("Even nums: ", even_arr)