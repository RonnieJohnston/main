#Ronnie Johnston
first_array = []
second_array = []
combined_array = []
#First loop, get first array input
for i in range(5):
    temp = input('Enter a number for the first list: ')
    temp = int(temp)
    first_array.append(temp)

#Second loop, get second array input
for i in range(5):
    temp = input('Enter a number for the second list: ')
    temp = int(temp)
    second_array.append(temp)

#Third loop, selects an int from the first array and compares it to each int in the second array.
#If there's a match, it's added to the combined array
for i in range(5):
    if first_array[i] in second_array:
        combined_array.append(first_array[i])

print("First list: ", first_array)
print("Second list: ", second_array)
print("Common list: ", combined_array)