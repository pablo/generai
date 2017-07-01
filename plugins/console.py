from helper import print_dice, print_dice_val, print_scoresheets
import string

def name():
    return "CONIO"


# this plugin uses console I/O to make plays

def roll_dice_eval(roll_dice):
    return [int(x) - 1 for x in list(roll_dice)]

def play(roll_no, dice, bonus, players, scoresheets):
    print_scoresheets(scoresheets)
    print("Roll: {0}".format(roll_no))
    print_dice(dice)
    roll_dice = input("Levantar dados? ") if roll_no < 2 else None
    if roll_dice:
        return roll_dice_eval(roll_dice), None, None
    else:
        decision = raw_input("jugada? ")
        scoresheet = int(raw_input("casilla {0}? ".format(str(list(range(len(scoresheets)))))))
        return ([], decision, scoresheet)
