import random
import string
from words import words


def is_invalid_word(word):
    while '-' in word or ' ' in word:
        return True
    return False


def hangman():
    word = '-'
    while is_invalid_word(word):
        word = random.choice(words).upper()

    word_letters = set(word)
    alphabet_letters = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while(len(word_letters) > 0 and lives != 0):
        
        print('Used letters: ',' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("You have", lives,"lives left. The Word is:"," ".join(word_list))
        
        guessed_letter = input("\nEnter an alphabet guess: ").upper()
        
        if guessed_letter in alphabet_letters - used_letters:
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
            else:
                lives -= 1
            used_letters.add(guessed_letter)
        elif guessed_letter in used_letters:
                print("You have already used this letter!")
        else:
            print("Oh No! Please enter a valid alphabet.")


    if lives != 0:
        print(f"\nYay! You have guessed {word}")
    else:
        print(f"Better luck next time the word was: {word}")


hangman()