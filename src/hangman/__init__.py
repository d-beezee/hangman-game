import random
from hangman.hangman import print_hanged_man

def start(wordlist,retries):
    """Entry point for the application script"""
    word = random.choice(wordlist)
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = retries
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:", main+"\n")
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character:\n")
            guess = input()

        if guess not in word:
            turns = turns - 1
            game_over = print_hanged_man(turns)
            if game_over :
            	break 
