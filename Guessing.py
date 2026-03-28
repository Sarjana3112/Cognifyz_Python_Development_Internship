import random

low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))

number = random.randint(low, high)
guess = None

print(f"Guess the number between {low} and {high}")

while guess != number:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Correct Guess!")