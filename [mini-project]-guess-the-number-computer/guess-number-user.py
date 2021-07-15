# Computer will generate some random number and user has to guess it in 3 attempts
# Computer should generate some hints on the range of number
import random


def guess(maximum):
    secret_number = random.randint(1, maximum)
    guessed_number = 0
    max_guess_count = 3
    guess_count = max_guess_count

    print(f"Guess a number in {guess_count} attempts\n")
    
    while(guess_count):
        guessed_number = int(input(f"Guess a number between 1 to {maximum}: "))
        if guessed_number > secret_number:
            print("Sorry, Guessed number too high! \n")
        elif guessed_number < secret_number:
            print("Sorry, Guessed number is too low\n")
        else:
            print(f"\nGood! You have guessed the number {secret_number} correctly!!\n")
            break
        guess_count -= 1

    else:
        print(f"\nSorry you only get {max_guess_count} attempts.\n{secret_number} was the secret number")

guess(10)