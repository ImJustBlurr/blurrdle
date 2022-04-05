import os
import sys
import random
import time
from colorama import *

#initializing colorama
init()
logfile = open("C:/Users/morni/Desktop/Code/blurrdle/log.txt","a")
logfile.truncate(0)
os.system('cls' if os.name == 'nt' else 'clear')
#VARIABLES
i = 1
c = -1
win = False
reset = Style.RESET_ALL
wordleArray = []
guessArray = []

#getting word
with open("C:/Users/morni/Desktop/Code/blurrdle/actualwordbank.txt", "r") as file:
    allActualText = file.read()
    actualWords = list(map(str, allActualText.split()))

with open("C:/Users/morni/Desktop/Code/blurrdle/potentialwordbank.txt", "r") as file:
    allPotentialText = file.read()
    potentialWords = list(map(str, allPotentialText.split()))

wordle = random.choice(actualWords)
for letter in wordle:
    wordleArray.append(letter)

#print(Fore.RED + wordle)

#prompt
print(Fore.CYAN + ' _     _                    _ _      \n| |__ | |_   _ _ __ _ __ __| | | ___ \n| \'_ \\| | | | | \'__| \'__/ _` | |/ _ \\\n| |_) | | |_| | |  | | | (_| | |  __/\n|_.__/|_|\\__,_|_|  |_|  \\__,_|_|\\___|')
print(Style.RESET_ALL)

while i < 7:
    
    print(f'{i}/6:', end=' ')
    guess = input().lower()
    logfile.write(f'{guess}\n')
    for letter in guess:
        guessArray.append(letter)
    print ("\033[A                             \033[A")

    if len(guess) < 5 or len(guess) > 5:
        print(Fore.RED + 'Your guess must be 5 letters long. Try again.' + reset)
        time.sleep(1)
        print ("\033[A                                             \033[A")
        guessArray.clear()
        continue

    if guess not in potentialWords:
        print(Fore.RED + 'Your word is not in our dictionary. Try again.' + reset)
        time.sleep(1)
        print ("\033[A                                              \033[A")
        guessArray.clear()
        continue

    elif guess == wordle:
        print(f'{i}/6:', end=' ')
        print(Fore.GREEN + guess + reset)
        print(Fore.GREEN + '\nYOU SUCCESSFULLY GUESSED THE WORDLE' + reset)
        win = True
        if win == True:
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
            continue
        elif reiterate == 'n':
            break
    print(f'{i}/6:', end=' ')
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

    if i == 6:
        if win == False:
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

#deinitializing colorama
logfile.write(f'\nSolution: {wordle}')
logfile.close()
deinit()
