import random

number_to_guess = random.randrange(100)
user_number = 0
numberOfAttempts = 0

def check_value(number):
    if number > number_to_guess:
        print("To high!")
    elif number < number_to_guess:
        print("To low!")
    else:
        print("Correct!")
        print("Took you " + str(numberOfAttempts) + " attempts")


print("Guess a number between 1 and 100")
while (user_number != number_to_guess): 
    user_number = int(input("Your hint: "))
    check_value(user_number)
    numberOfAttempts+=1




    


