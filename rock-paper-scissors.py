from random import randint

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    play = input('Do you want to play(again)? Y|N\n')

    if play.lower() == 'n':
        print('Closing...')
        exit(0)
    print("Enter your choice\n"
          +"1 - Rock\n"
          +"2 - Paper\n"
          +"3 - Scissors\n")
    
    choice = int(input('Enter a valid choice: '))
    while choice < 1 or choice > 3:
        choice = int(input('Invalid choice, reenter please'))

    #Player
    if choice == 1: choice_name = 'Rock' 
    elif choice == 2: choice_name = 'Paper' 
    else: choice_name = 'Scissors'
    #Machine
    comp_choice = randint(1, 3)
    if comp_choice == 1: comp_choice_name = 'Rock' 
    elif comp_choice == 2: comp_choice_name = 'Paper' 
    else: comp_choice_name = 'Scissors'


    print('You chose '+choice_name+', Machine chose' +comp_choice_name)

    #win/lose
    if choice == comp_choice: print('DRAW')
    elif (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 1): print('YOU WIN!!!')
    else: print('YOU LOSE!!!')
