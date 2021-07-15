# binary search game with computer, let the computer guess

from math import ceil, floor, log2
from random import random

def guess(maximum):
    low = 1
    high = maximum
    feedback = ''

    print(f'Think of a number between 1 and {high} and I will guess it in {ceil(log2(high))} attempts for sure!')

    while(feedback != 'c'):
        guessed_number = floor((low+high)/2)
        print(f'Guessed number: {guessed_number} ?')
        feedback = input("Is the number too high(H), too low(L) or correct(C)? ").lower()
        if feedback == 'l':
            low = guessed_number + 1
        elif feedback == 'h':
            high = guessed_number - 1

    print("Computer have guessed it correctly!!")


maximum = int(input('What should be the max range: '))
guess(maximum)