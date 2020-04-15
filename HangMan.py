#http://inventwithpython.com/invent4thed/chapter8.html

import random

HANGMAN_PICS=['''
   +---+
       |
       |
       |
      ===''', '''
    +---+
    0   |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''                               
    +---+
    0   |
   /|\  |
   /    |
       ===''','''                               
    +---+
    0   |
   /|\  |
   / \  |
       ===''']

words = """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox
         frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python 
         rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey 
         turtle weasel whale wolf wombat zebra""".split()


def getRandomWord(worldList):
    wordIndex=random.randint(0,len(worldList)-1)
    return worldList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('missedLetters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess=input()
        guess=guess.lower()
        if(len(guess) != 1):
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter choose again!')
        elif guess not in 'qwertyuiopasdfghjklçzxcvbnm':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you whant to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gamesIsDone = False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('Yes! You have found the secret word:' + secretWord)
            gamesIsDone=True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters,correctLetters,secretWord)
            print('You have run out of guesses! \nAfter '+
                str(len(missedLetters)) + ' missed guesses and ' +
                str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gamesIsDone=True

    
    if gamesIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters= ''
            gamesIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
                





    






