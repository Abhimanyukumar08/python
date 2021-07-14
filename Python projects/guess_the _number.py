import random

Easy_attempts = 10
Hard_attempts = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of the number between 1 to 100")
level= input("Chooes the diffculty. Type 'easy' or 'hard': ")
number = random.randint(1,100)
def guess_the_number(attempts):
    while attempts!=0:
        print("You have",attempts,"attempts remaining to guess the number: ")
        guess = int(input("Make a guess: "))
        if guess==number:
            print("You got it! The answer was", guess)
            break
        elif guess>number:
            print("Too High")
        elif guess<number:
            print("Too Low")
        elif attempts==0:
            print("You've run out of guesses, YOU LOSE")
        attempts -=1


if level=="hard":
    guess_the_number(Hard_attempts)
elif level=="easy":
    guess_the_number(Easy_attempts)

