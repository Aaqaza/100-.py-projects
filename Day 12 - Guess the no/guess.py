import random
from art import logo

print(logo)

print("Welcome to the number guessing game!\nI'm thinking of a number from 1 to 100")
level = input("Choose a difficulty level. Type easy or hard: ")

def compare(guess, no):
    """Compares the guess and the number chosen by the computer"""
    if guess > no:
        print("Too high")
    elif guess < no:
        print("Too low")
    else:
        print(f"You got it! The answer was {guess}")
        return True  # Signal that the correct guess was made
    return False

def make_a_guess(attempt):
    """Prints and accepts the guesses"""
    print(f"You have {attempt} attempts remaining to guess the number")
    return int(input("Make a guess: "))

no = random.randint(1, 100)

if level == "easy":
    attempt = 10
elif level == "hard":
    attempt = 5
else:
    print("Invalid difficulty level. Please choose easy or hard")

while attempt > 0:
    guess = make_a_guess(attempt)
    if compare(guess, no):
        break  # Exit the loop if the correct guess was made
    attempt -= 1

if attempt == 0:
    print(f"You ran out of guesses! The correct answer was {no}")
