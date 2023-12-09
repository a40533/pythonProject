print("Welcome to RollerCoaster!")
height = int(input("What is your Height. "))

if height >= 120:
    print("You are allowed to ride.")
    age = int(input("What is your age. "))
    if age < 7 or age > 45:
        print("You can ride for free.")
    elif age <= 12 & age > 7:
        print("Please pay $5.")
    elif age <= 18 & age > 12:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("You are not allowed to ride.")
