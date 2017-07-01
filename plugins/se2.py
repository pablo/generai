
def name():
    return "SERIAL 2"


# this plugin will play serially to the next available free space
# in its corresponding scoresheet

def play(roll_no, dice, bonus, players, scoresheets):
    # where

    i = 0
    for ss in scoresheets:
        my_ss = ss[name()]
        if '4' not in my_ss:
            return [], '4', i
        elif '5' not in my_ss:
            return [], '5', i
        elif '6' not in my_ss:
            return [], '6', i
        elif 'ESCALERA' not in my_ss:
            return [], 'ESCALERA', i
        elif 'FULLHOUSE' not in my_ss:
            return [], 'FULLHOUSE', i
        elif 'POKER' not in my_ss:
            return [], 'POKER', i
        elif 'GENERALA' not in my_ss:
            return [], 'GENERALA', i
        i = i + 1
