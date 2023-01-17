#Ronnie Johnston
#Get user input
user_input1 = input("Enter a string: ")
user_input2 = input("Enter another string: ")
#Check if first string is contained in second string and vice-versa
#https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
if user_input1 in user_input2:
    print('True')
elif user_input2 in user_input1:
    print('True')
else:
    print('False')