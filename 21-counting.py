def player_lose():
    print('\nYOU LOSE')
    exit(0)

def consecutive(numbers):
    length = len(numbers)
    for i in range(1, length):
        if numbers[i] - numbers[i-1] != 1:
            return False
    return True

def start_game():
    numbers = []
    last = 0
    while True:
        chance = input('Do you want to go first? Y|N ')
        if chance.upper() == 'Y':
            while True:
                #Player
                if last == 20: player_lose()

                inp = int(input('How many numbers do you want to enter? 1-3: '))
                if inp < 1 or inp > 3:
                    print('Invalid, you are disqualified')
                    exit(0)
                
                print('Enter your numbers:')
                for _ in range(inp):
                    numbers.append(int(input('> ')))
                if not consecutive(numbers):
                    print("You didn't enter consecutive numbers")
                    player_lose()
                last = numbers[-1]

                #Machine
                comp = 4 - inp
                for i in range(1, comp + 1):
                    numbers.append(last + i)
                last = numbers[-1]
                print("Numbers after machine's turn\n", numbers)

        elif chance.upper() == 'N': 
           
            last = 0
            comp = 1
            while last < 20:
                #Machine
                print("\nMachine's turn:")
                for i in range(1, comp+1):
                    numbers.append(last + i)
                print("Numbers after machine's turn\n", numbers)
                last == numbers[-1]
                if last == 20: player_lose()

                #Player
                inp = int(input('How many numbers do you want to enter? 1-3: '))
                if inp < 1 or inp > 3:
                    print('Invalid, you are disqualified')
                    exit(0)
                
                print('Enter your numbers:')
                for _ in range(inp):
                    numbers.append(int(input('> ')))
                if not consecutive(numbers):
                    print("You didn't enter consecutive numbers")
                    player_lose()
                last = numbers[-1]

                #Machine
                comp = 4 - (last % 4)
                if comp == 4: comp = 3

            print("\nCONGRATULATIONS!!!")
            print("YOU WON!")
            exit(0)
        else:
            print('Wrong choice, please enter Y or N')





            

game = True
while game:
    print('Player 2 is Machine')
    ans = input('Do you want to play? Y|N ')
    if ans.upper() == 'N':
        print('Quitting...')
        exit(0)
    else:
        start_game()