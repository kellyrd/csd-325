"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}

# -----------------------------
# FUNCTIONS
# -----------------------------

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def show_dice_shake():
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

def get_Cho_Han():
    while True:
        player_choice = input('> ').upper()
        if player_choice != 'CHO' and player_choice != 'HAN':
            print('Please enter either "CHO" or "HAN".')
        else:
            return player_choice

def determine_correct_bet(dice1, dice2):
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        return 'CHO'
    else:
        return 'HAN'

def apply_results(purse, pot, playerWon):
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)
    else:
        print('You lost!')
        purse = purse - pot
    return purse

def get_bet(purse):
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            return int(pot)

# -----------------------------
# INTRO TEXT
# -----------------------------

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

# -----------------------------
# MAIN GAME LOOP
# -----------------------------

purse = 5000

while True:
    pot = get_bet(purse)
    show_dice_shake()

    player_choice = get_Cho_Han()
    
    dice1, dice2 = roll_dice()

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    
    correctBet = determine_correct_bet(dice1, dice2)
    playerWon = (player_choice == correctBet)

    purse = apply_results(purse, pot, playerWon)

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
