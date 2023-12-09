import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock, Paper, Scissors]
computer = random.randint(0, 2)
print("0 -> Rock\n1 -> Paper\n2 -> Scissors")
my_choice = int(input("What is your choice: "))
if 3 < my_choice < 0:
    print("Invalid Input, You lose")
else:
    print(game_images[my_choice])
    print("Computer chose:")
    print(game_images[computer])

if my_choice == computer:
    print("It's a draw.")
if my_choice == 0 and computer == 1:
    print("You lose")
if my_choice == 0 and computer == 2:
    print("You win")
if my_choice == 1 and computer == 0:
    print("You win")
if my_choice == 1 and computer == 2:
    print("You lose")
if my_choice == 2 and computer == 0:
    print("You lose")
if my_choice == 2 and computer == 1:
    print("You win")
