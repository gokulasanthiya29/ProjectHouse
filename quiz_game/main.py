# My first coding project

player_name = input('Enter your name: ')
print('Hi ' + player_name + ', Welcome to the Quiz!')

play = input("Are you interested to play? ")
if play.upper() != "YES":
    quit()

print("Great! Let\'s play :) ")
score = 0

reply = input("What does API stand for? ")
if reply.upper() == "APPLICATION PROGRAMMING INTERFACE":
    print("You\re right!")
    score += 1
else:
    print("Oh, no! :( ")

reply = input("What does WSGI stand for? ")
if reply.upper() == "WEB SERVER GATEWAY INTERFACE":
    print("You\re right!")
    score += 1
else:
    print("Oh, no! :( ")
    
reply = input("What does HCI stand for? ")
if reply.upper() == "HUMAN COMPUTER INTERACTION":
    print("You\re right!")
    score += 1
else:
    print("Oh, no! :( ")
    
reply = input("What does GPU stand for? ")
if reply.upper() == "GRAPHICS PROCESSING UNIT":
    print("You\re right!")
    score += 1
else:
    print("Oh, no! :( ")
    
print('You got ' + str(score) + ' questions, correct!')
print('You got ' + str(((score*20)/80)*100) + '%.')

    
