import random
import os

def display(lives, hangman = [], missedGuess = [], guessString = []):
    os.system('clear || cls')  #For Linux/OS X
    print("Lives: ", lives)
    print(''.join([char if (char == ' ' or char == '\n' or (int(char) < (10 - lives))) else ' ' for char in hangman])) #prints the hangman base on how many life is left.
<<<<<<< HEAD
    print("Inccorect guess: " , ','.join(missedGuess))
=======
    print("Incorrect guess: " , ','.join(missedGuess))
>>>>>>> 1fa3b501741d8e6657b2183a7ac9bb46c31cd4ce
    print(' '.join(guessString))

dictionary = open("dictionary.txt").read().split("\n")
hangman = list("""\
    22222222222222
    1     3     2
    1   3       4
    1 3       4   4
    1           4
    1          657
    1         6 5 7
    1        6  5  7
    1          8 9
    1         8   9
    1        8     9
    1       8       9
    1
    1
000000000
""")

word = dictionary[random.randrange(0, len(dictionary))]
guessString = list("_" * len(word))
missedGuess = [] #letters the user has guessed
lives = 10


display(lives, hangman, missedGuess, guessString)
while lives > 0 and '_' in guessString:
    guess = input('Enter guess: ').lower()
<<<<<<< HEAD

    if (guess.isalpha()) and (not guess in missedGuess):
=======

    if (guess.isalpha()) and (not guess in missedGuess):

>>>>>>> 1fa3b501741d8e6657b2183a7ac9bb46c31cd4ce
        if guess == word: #Correct Guess
            guessString = word
        elif len(guess) == 1 and guess in word: #Correct Guess
            guessString = [word[i] if word[i] == guess else char for i, char in enumerate(guessString)] #replaces the character in the guessString with correctly guessed letter
        else: #Incorrect Guess
            missedGuess.append(guess)
            lives = lives - 1

    display(lives, hangman, missedGuess, guessString)

print("You won!" if lives > 0 else "You lost!\nCorrect word: {correctWord}".format(correctWord = word)) #Python is fucking ridiculous
