# Kelly Dimick
# 09/07/2026
# Assignment 1.3

# Input from user for number of beers
# X bottles of beer on the wall, X bottles of beer, take one down and pass it around, 
# Remove 1 beer (X = X - 1)
# X bottles of beer on the wall.
# Is X greater than 0
# If x greater than 0 repeat
# If x is not greater than 0
# Time to buy more beer

bottles = int(input("How many bottles of beer? "))

def number_of_beers(bottles):
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, ")
        bottles = bottles - 1
        print(f"{bottles} bottles of beer on the wall.")
        
    print("Time to buy more bottles of beer.")
number_of_beers(bottles)