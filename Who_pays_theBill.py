import random

names = input("Give all your names: ")
name = names.split(", ")
i = random.randint(0, len(name) - 1)
payer = name[i]
print(payer + " will pay the bill today")
