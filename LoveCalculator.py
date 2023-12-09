first_name = input("What is your name? ")
second_name = input("What is your potential partner's name? ")
first_name_lower = first_name.lower()
second_name_lower = second_name.lower()
combined_name= first_name_lower + second_name_lower
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_number = t+r+u+e
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
second_number = l+o+v+e
love_score = str(first_number)+str(second_number)
print("Your score is {love_score}")

