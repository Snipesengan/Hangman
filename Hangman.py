import random
import os

def display(lives, hangman = [], alphabetSoup = [], guessString = []):
    os.system('clear')  #For Linux/OS X
    print("Lives: ", lives)
    print(''.join([char if (char == ' ' or char == '\n' or (int(char) < (10 - lives))) else ' ' for char in hangman])) #prints the hangman base on how many life is left.
    print("Inccorect guess: " , ','.join([letter for letter in alphabetSoup if (not letter in word)]))
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
alphabetSoup = [] #letters the user has guessed
lives = 10

display(lives, hangman, alphabetSoup, guessString)
while lives > 0 and '_' in guessString:
    guessChar = input('Enter guess: ').lower()

    if (guessChar.isalpha()) and (len(guessChar) == 1) and (guessChar.islower()) and (not guessChar in alphabetSoup):
        alphabetSoup.append(guessChar)
        if guessChar in word: #Correct Guess
            guessString = [word[i] if word[i] == guessChar else char for i, char in enumerate(guessString)] #replaces the character in the guessString with correctly guessed letter
        else: #Incorrect Guess
            lives = lives - 1

    display(lives, hangman, alphabetSoup, guessString)

print("You won!" if lives > 0 else "You lost!\nCorrect word: {correctWord}".format(correctWord = word)) #Python is fucking ridiculous
