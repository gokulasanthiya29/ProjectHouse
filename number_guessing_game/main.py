import random

guesses = 0

top_of_range = input('Until which number do you wanna guess? ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Enter a number larger than 0 next time :( ')
        quit()
else:
    print('Enter a positive integer next time :( ')
    quit()
    
random_number = random.randint(1, top_of_range)

while True:
    guesses += 1
    
    user_guess = input('Make a guess! ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print('Enter a positive integer next time :( ')
        continue
    
    if user_guess == random_number:
        print('Well done! :) ')
        break
        
    elif user_guess > random_number:
        print("You were above the number :o ")
    
    else:
        print("You are below the number :o ")    
    
print('You got it right in', guesses, 'guesses!')




