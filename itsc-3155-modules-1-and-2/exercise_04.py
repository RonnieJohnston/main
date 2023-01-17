#Ronnie Johnston
#https://www.geeksforgeeks.org/python-initialize-empty-array-of-given-length/
#Initialize an empty array
num_array = []
sum = 0
#Get user input and convert to integer
count = input("Enter amount of floats: ")
count = int(count)
#First for loop, get input for each number, convert to float, and add to array
for i in range(count):
    temp = input("Enter number " + str(i+1) + ": ")
    temp = float(temp)
    num_array.append(temp)

#Second for loop, add up all the floats and store them
for i in range(count):
    sum = sum + num_array[i]
#Compute average and print
average = (sum / count)
print("List: ", num_array)
print("Average: ", average)