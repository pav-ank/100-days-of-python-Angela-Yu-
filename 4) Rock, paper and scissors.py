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

import random

game = [rock, paper, scissors]
print("Welcome to RPS game ")

human_choice = int(input("What do you choose? type 0 for Rock, 1, for Paper, and 2 for Scissors: "))

if human_choice >= 0 and human_choice <= 2:
    print(game[human_choice])
computer_choice = random.randint(0, 2)
print(game[computer_choice])

if human_choice >= 3 or human_choice < 0:
    print("Enter a valid number")
elif human_choice == 0 and computer_choice == 2:
    print("You win")
elif human_choice == 2 and computer_choice == 0:
    print("You lose")
elif human_choice < computer_choice :
    print("You lose")
elif human_choice > computer_choice:
    print("You win")
elif human_choice == computer_choice:
    print("It's a draw")

