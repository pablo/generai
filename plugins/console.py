from helper import print_dice, print_dice_val, print_scoresheets
import string

def name():
    return "CONIO_1.0"


# this plugin uses console I/O to make plays

def roll_dice_eval(roll_dice):
    return [int(x) - 1 for x in roll_dice if x in string.digits]

def play(roll_no, dice, bonus, players, scoresheets):
    if roll_no == 0:
        print_scoresheets(scoresheets)
    print("Roll: {0}".format(roll_no))
    print_dice(dice)
    roll_dice = input("Levantar dados? ") if roll_no < 2 else None
    if roll_dice:
        return roll_dice_eval(roll_dice), None, None
    else:
        decision = input("jugada? ")
        scoresheet = int(input("casilla? "))
        return ([], decision, scoresheet)
