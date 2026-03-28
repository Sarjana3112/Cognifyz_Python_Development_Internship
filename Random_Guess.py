import random

number = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations! You guessed the correct number.")