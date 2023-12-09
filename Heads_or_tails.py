import random

choice = int(input("Heads(0) or Tails(1): "))
random_number = random.randint(0, 1)
if choice == random_number:
    print("You win.")
else:
    print("You lose.")

