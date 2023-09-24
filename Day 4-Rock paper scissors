import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user > 2 or user < 0:
  print("Invalid choice, You lose")
else:
  print(options[user])
  
  computer = random.randint(0,2)
  print("Computer chose" + options[computer])
  
  if user == 0 and computer == 2:
    print("You win!")
  elif computer == 2 and user == 0:
    print("You lose")
  elif computer > user:
    print("You lose")
  elif user > computer:
    print("You win")
  elif computer == user:
    print("It's a draw")

