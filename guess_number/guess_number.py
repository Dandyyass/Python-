import random 


secret = random.randint(1, 50)
tries = 5

while tries > 0:
    guess = int(input("Guess a number between 1 and 50 (Tries left: {}): ".format(tries)))
    tries -= 1

    if guess == secret:
        print("Correct! You guessed it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    if tries == 0:
        print("Game over! The number was:", secret)