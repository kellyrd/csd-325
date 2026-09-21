"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}

# When making these enhancements I wanted to make sure that I left the code better than I found it and that I implemented ETC.
# I knew right away I wanted to break the code out into functions. I made my functions and then copied and pasted into CoPilot to make sure that I was doing it correctly. Once I was finished I copied and pasted all my code and put into CoPilot to make sure it was correct, easy to read and formated correctly.

# -------------------------------------------------------------
# PROGRAM MODIFICATIONS (by KRD)
#
# This version of the Cho-Han game includes several enhancements
# and structural improvements beyond the original implementation.
#
# 1. Reorganized Code Structure:
#    - All major game actions were moved into separate functions
#      (roll_dice, show_dice_shake, get_Cho_Han, determine_correct_bet,
#      apply_results, get_bet) to improve readability and modularity.
#
# 2. Updated Input Prompt:
#    - All user input prompts now use my initials ("krd:") instead of
#      the original ">" prompt for personalization.
#
# 3. Updated House Fee:
#    - The house fee was changed from 10% to 12%.
#    - Fee calculation now uses: fee = int(pot * 0.12)
#
# 4. Added Bonus Rule:
#    - If the dice total is 2 or 7, the player receives a 10-mon bonus.
#    - Bonus is applied immediately after dice reveal and before
#      win/loss resolution.
#
# 5. Updated Intro Text:
#    - Intro now includes a description of the new bonus rule.
#
# -------------------------------------------------------------

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
        player_choice = input('krd: ').upper() # CHANGE: Updated input prompt to my initials (krd)
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

        fee = int(pot * 0.12) # CHANGE: Updated house fee from 10% to 12%
        print('The house collects a', fee, 'mon fee.')
        purse -= fee
 
    else:
        print('You lost!')
        purse = purse - pot

    return purse

def get_bet(purse):
    print('You have', purse, 'mon. \nHow much do you want to bet? (or QUIT)')
    while True:
        pot = input('krd: ') # CHANGE: Updated input prompt to my initials (krd)
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

BONUS RULE: If the dice total is 2 or 7, you receive a 10-mon bonus! 
''')
# CHANGE: Added intro text describing bonus rule

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
    print()

    total = dice1 + dice2 # CHANGE: Added bonus rule for totals of 2 or 7 (+10 mon)
    if total == 2 or total == 7:
        print(f'Bonus! The total was {total}. You receive a 10-mon bonus!')
        purse += 10

    correctBet = determine_correct_bet(dice1, dice2)
    playerWon = (player_choice == correctBet)

    purse = apply_results(purse, pot, playerWon)
    print()

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
