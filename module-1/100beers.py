# Kelly Dimick
# 09/07/2026
# Assignment 1.3 100 Bottles of Beer

# This program asks the user for number of Bottles of Beer (1-100) on the wall and then it counts down to zero, then informing user more beer is needed.

while True:
    try:
        bottles = int(input("How many bottles of beer? "))

        if 1 <= bottles <= 100: # User technically can choose more than 100 but to stick to the original song, I'm restricting it to no more than 100.
            break
        else:
            print("Please enter a number between 1 and 100.")

    except:
        print("Invalid input. Please enter a whole number.")

def number_of_beers(bottles):
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, ")

        bottles = bottles - 1
        print(f"{bottles} bottles of beer on the wall.")

    print("Time to buy more bottles of beer.")

number_of_beers(bottles)