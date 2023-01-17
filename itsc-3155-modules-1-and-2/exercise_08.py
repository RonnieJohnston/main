#Ronnie Johnston
total_arr = []
once_arr = []
#Take user input 10 times
for i in range(10):
    user_input = input("Enter number " + str(i + 1) + ":")
    user_input = int(user_input)
    #If input hasn't been recorded yet, put it in the 'one time' array
    if user_input not in total_arr:
        once_arr.append(user_input)
    #But if the input has been recorded, and it's in the 'one time' array, remove it from the 'one time' array
    elif user_input in total_arr and user_input in once_arr:
        once_arr.remove(user_input)
    #Then, record it in the total array
    total_arr.append(user_input)

print("Original List: ", total_arr)
print("Nums that only appear once: ", once_arr)


