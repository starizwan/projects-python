# A simple rock paper scissor game

import random

def is_win(user_chose, computer_chose):
    # r > s, s > p, p > r
    if ((user_chose == 'r' and computer_chose == 's') or 
    (user_chose == 's' and computer_chose == 'p') or 
    (user_chose == 'p' and computer_chose == 'r')):
        return True

def game():
    options = ['r', 'p', 's']
    user_chose = input('(R)ock, (P)aper, (S)cissor: ').lower()
    computer_chose = random.choice(options)

    if(user_chose == computer_chose):
        print("It is tie :) ")
        return 

    elif (is_win(user_chose, computer_chose)):
        print("Yay! User Won!!")
        return 
    
    print("Oh No Computer Won Again :(")

game()