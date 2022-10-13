import os
import sys
import random
import time
from colorama import *

#initializing colorama
init()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#setting up the log file
#log file is there for the case of a crash. you will be able to see what the word was if something glitches.
logfile = open(os.path.join(__location__, 'log.txt'), 'a')
logfile.truncate(0)

os.system('cls' if os.name == 'nt' else 'clear') #clears the terminal

#VARIABLES
i = 1 #iteration for main guessing loop
c = -1 #iteration through chars in the guess
reset = Style.RESET_ALL #used with colorama to reset the styles
wordleArray = []
guessArray = []

#getting word
with open(os.path.join(sys.path[0], "actualwordbank.txt"), "r") as file:
    allActualText = file.read()
    actualWords = list(map(str, allActualText.split()))

with open(os.path.join(sys.path[0], "potentialwordbank.txt"), "r") as file:
    allPotentialText = file.read()
    potentialWords = list(map(str, allPotentialText.split()))

wordle = random.choice(actualWords)
for letter in wordle:
    wordleArray.append(letter)

#prompt
print(Fore.CYAN + ' _     _                    _ _      \n| |__ | |_   _ _ __ _ __ __| | | ___ \n| \'_ \\| | | | | \'__| \'__/ _` | |/ _ \\\n| |_) | | |_| | |  | | | (_| | |  __/\n|_.__/|_|\\__,_|_|  |_|  \\__,_|_|\\___|')
print(Style.RESET_ALL)

#main guessing loop
while i < 7:
    
    print(f'{i}/6:', end=' ')
    guess = input().lower()
    for letter in guess:
        guessArray.append(letter)
    print ("\033[A                             \033[A")

    if len(guess) < 5 or len(guess) > 5: #error for != 5 letter word
        print(Fore.RED + 'Your guess must be 5 letters long. Try again.' + reset)
        time.sleep(1)
        print ("\033[A                                             \033[A")
        guessArray.clear()
        continue

    if guess not in potentialWords: #error for an invalid word
        print(Fore.RED + 'Your word is not in our dictionary. Try again.' + reset)
        time.sleep(1)
        print ("\033[A                                              \033[A")
        guessArray.clear()
        continue

    elif guess == wordle: #checks if they guessed the word
        print(f'{i}/6:', end=' ')
        print(Fore.GREEN + guess + reset)
        print(Fore.GREEN + '\nYOU SUCCESSFULLY GUESSED THE WORDLE' + reset)
        print(Fore.CYAN + 'THE WORD WAS: ' + Fore.GREEN + wordle + reset)
        print(Fore.CYAN + 'If you would like to play again type ' + Fore.GREEN + 'y' + Fore.CYAN + ', if not type ' + Fore.RED + 'n' + Fore.CYAN + '.' + reset)
        reiterate = input().lower()
        if reiterate == 'y': #asks if they want to play again
            i = 1
            c=-1
            guessArray.clear()
            wordleArray.clear()
            wordle = random.choice(actualWords)
            for letter in wordle:
                wordleArray.append(letter)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN + ' _     _                    _ _      \n| |__ | |_   _ _ __ _ __ __| | | ___ \n| \'_ \\| | | | | \'__| \'__/ _` | |/ _ \\\n| |_) | | |_| | |  | | | (_| | |  __/\n|_.__/|_|\\__,_|_|  |_|  \\__,_|_|\\___|\n' + reset)
            continue
        elif reiterate == 'n':
            break
    print(f'{i}/6:', end=' ') #processes the word and checks if the guess has any valid letters in the wordle and if they're in the right position.
    for letter in guess:
        c+=1
        if guessArray[c] == wordleArray[c]:
            
            color = Fore.GREEN
            print(color + letter + reset, end='')
            #c=-1
            continue

        if letter in wordleArray:
            
            color = Fore.YELLOW
            print(color + letter + reset, end='')
            #c=-1
            continue
        print(letter, end='')
        
    print('\n')
    logfile.write(f'{guess}\n')

    if i == 6: #displays when the user is out of guesses and didnt get the word right.
            print(Fore.CYAN + 'THE WORD WAS: ' + Fore.GREEN + wordle + reset)
            print(Fore.CYAN + 'If you would like to play again type ' + Fore.GREEN + 'y' + Fore.CYAN + ', if not type ' + Fore.RED + 'n' + Fore.CYAN + '.' + reset)
            reiterate = input().lower()
            
            if reiterate == 'y':
                i = 1
                c=-1
                guessArray.clear()
                wordleArray.clear()
                wordle = random.choice(actualWords)
                for letter in wordle:
                    wordleArray.append(letter)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.CYAN + ' _     _                    _ _      \n| |__ | |_   _ _ __ _ __ __| | | ___ \n| \'_ \\| | | | | \'__| \'__/ _` | |/ _ \\\n| |_) | | |_| | |  | | | (_| | |  __/\n|_.__/|_|\\__,_|_|  |_|  \\__,_|_|\\___|\n' + reset)
                logfile.truncate(0)
                continue
            elif reiterate == 'n':
                pass

    i += 1
    c=-1
    guessArray.clear()

#deinitializing colorama and closing log file.
logfile.write(f'\nSolution: {wordle}')
logfile.close()
deinit()
