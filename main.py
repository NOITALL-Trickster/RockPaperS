import random
from html import entities

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")

choice = int(input())
computer_choice = random.randint(0,2)
entity = [rock,paper,scissors]

if 0 < choice < 3:
    print(entity[choice] + "\n")
    print("Computers choice: ")
    print(entity[computer_choice] + "\n")

    if choice == computer_choice:
        print("It's a tie!")
    else:
        if choice == 0:
            if computer_choice == 1:
                print("Computers wins!")
            else:
                print("You win!")
        if choice == 1:
            if computer_choice == 0:
                print("You win!")
            else:
                print("Computers wins!")
        if choice == 2:
            if computer_choice == 0:
                print("Computers wins!")
            else:
                print("You win!")
else:
    print("Invalid choice!")

