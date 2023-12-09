print("Welcome to Python Pizza Deliveries!")
size = input("What is the size of the pizza? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y/N: ")
extra_cheese = input("Do you want extra cheese? Y/N: ")
if size == 'S' or size == 's':
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        if extra_cheese == 'Y' or extra_cheese =='y':
            print("Your bill is $20")
        print("Your bill is $17")
    print("Your bill is $15")
