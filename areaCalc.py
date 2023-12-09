def numOfCans(a, b, c):
    d = (a * b) / c
    return round(d)


coverage = 5
height = int(input("What is the height of your wall?"))
width = int(input("What is the width of your wall?"))
Required = numOfCans(height, width, coverage)
print(f"{Required} cans are required to paint the wall.")
