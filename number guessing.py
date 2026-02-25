from random import randint

low, high = map(int, input("Range: ").split())
answer = randint(low, high)

print("Good luck!")
guesses = 0
while True:
    guess = int(input("Your guess: "))

    if guess == answer:
        print("Correct, the answer is:", answer)
        print("You took", guesses, "guesses")
        break
    elif guess < answer:
        print("Too low, guess again")
        guesses += 1
    else:
        print("Too high, guess again")
        guesses += 1