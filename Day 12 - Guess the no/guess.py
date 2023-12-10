import random

print("Welcome to the number guessing game!\nI'm thinking of a number from 1 to 100")
level = input("Choose a difficulty level. Type easy or hard : ")

def compare(guess, attempt):
  """Compares the guess and the no chosen by the computer"""
  if guess > no:
    print("Too high")
  elif guess < no:
    print("Too low")
  elif guess == no:
   print(f"You got it! The answer was {guess}")
  if (attempt) == 1:
    print("You ran out of guesses! Better luck next time!")
  return

def make_a_guess(attempt):
  """Prints and accepts the guesses"""""
  while(attempt > 0):
    print(f"You have {attempt} attempts remaining to guess the no")
    guess = int(input("Make a guess: "))
    return guess

no = random.randint(1,100)

if level == "easy":
  attempt = 10
  while attempt != 0:
    guess = make_a_guess(attempt)
    compare(guess, attempt)
    attempt -= 1

elif level == "hard":
  attempt = 5
  while attempt != 0:
    guess = make_a_guess(attempt)
    compare(guess, attempt)
    attempt -= 1

else:
  print("Invalid difficulty level. Please choose easy or hard")
