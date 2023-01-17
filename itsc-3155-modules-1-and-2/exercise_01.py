#Ronnie Johnston
#Most of the exercise work uses references from the intro to Python slides
my_char = ''

#Get user input
user_input = input("Enter a grade from 0 to 100: ")
#Convert to integer
user_input = int(user_input)
#Line of if statements to determine letter grade using boolean statements
if (user_input >= 0 and user_input < 60):
    my_char = 'F'
elif (user_input >= 60 and user_input < 70):
    my_char = 'D'
elif (user_input >= 70 and user_input < 80):
    my_char = 'C'
elif (user_input >= 80 and user_input < 90):
    my_char = 'B'
elif (user_input >= 90 and user_input <= 100):
    my_char = 'A'

print('Your grade is a(n) ' + my_char)