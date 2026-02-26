from random import choice

words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
word_lst = words.split()
word = choice(word_lst)

chances = len(word) + 2
print("Don't get hanged! HINT: IT'S A FRUIT")
guesses = ''
while chances > 0:
    failed = 0
    for char in word:
        if char not in guesses:
            print('_', end = '')
            failed += 1
        else:
            print(char, end = '')
    print()
    if failed == 0: 
        print('You survived! Indeed, the word is', word)
        break
    print()
    guess = input('Guess a letter: ')
    if guess not in guesses:
        guesses += guess
    else: 
        print('You already guessed that')
        continue
    if guess not in word:
        chances -= 1
        print('OOPS! You have', chances, 'left!')
    
if(chances == 0): print('You got hanged! The word was', word)