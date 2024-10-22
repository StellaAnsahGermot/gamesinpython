# Generate a random number
# loop
# Ask the user to make a guess
# if not a valid number
# print an error
# if number < guess
    # print is too low


import random
number_to_guess = random.randint(1,100)

try:
    guess = int(input('Guess the number between 1 and 100: '))
except ValueError:
    print('Please enter a valid number')

if guess < number_to_guess:
    print('Too low')

if guess > number_to_guess:
        print('Too high')
