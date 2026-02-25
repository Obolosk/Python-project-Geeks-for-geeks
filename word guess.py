from random import choice

name = input("May I know your name? ")
print('Good luck!', name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = choice(words)
print('Guess the word!')
guesses = ''
turns = 12


while turns > 0:
    failed = 0
    for char in word:
        if char in guesses: 
            print(char, end = ' ')
        else:
            print('_', end = ' ')
            failed += 1
    
    if failed == 0:
        print()
        print('YOU WIN, the word is:', word)
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print('Wrong, you have', turns, 'guess(es) left')

if turns == 0: print("YOU LOSE")