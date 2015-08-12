"""

|-----|
|     |
|  X  |
|     |
|-----|

|-----|
|X    |
|     |
|    X|
|-----|


|-----|
|X    |
|  X  |
|    X|
|-----|

|-----|
|X   X|
|     |
|X   X|
|-----|

|-----|
|X   X|
|  X  |
|X   X|
|-----|

|-----|
|X   X|
|X   X|
|X   X|
|-----|

"""

v_1 = """|-----|
|     |
|  X  |
|     |
|-----|
"""

v_2 = """|-----|
|X    |
|     |
|    X|
|-----|
"""

v_3 = """|-----|
|X    |
|  X  |
|    X|
|-----|
"""

v_4 = """|-----|
|X   X|
|     |
|X   X|
|-----|
"""

v_5 = """|-----|
|X   X|
|  X  |
|X   X|
|-----|
"""

v_6 = """|-----|
|X   X|
|X   X|
|X   X|
|-----|
"""

def print_dice_val(val):
    if val == 1:
        print(v_1)
    elif val == 2:
        print(v_2)
    elif val == 3:
        print(v_3)
    elif val == 4:
        print(v_4)
    elif val == 5:
        print(v_5)
    elif val == 6:
        print(v_6)


def print_dice(dice):
    for d in dice:
        print_dice_val(d)

def print_scoresheet_line(title, values):
    values_fmt = "{:>10}"*len(values)
    values_print = values_fmt.format(*values)
    print("{0:>10}{1}".format(title, values_print))

def print_scoresheets(scoresheets):
    _4 = []
    _5 = []
    _6 = []
    escalera = []
    fullhouse = []
    poker = []
    generala = []
    players = None
    for ss in scoresheets:
        players = sorted(ss.keys())
        for player in players:
            s = ss[player]
            _4.append(s['4'] if '4' in s else '_')
            _5.append(s['5'] if '5' in s else '_')
            _6.append(s['6'] if '6' in s else '_')
            escalera.append(s['ESCALERA'] if 'ESCALERA' in s else '_')
            fullhouse.append(s['FULLHOUSE'] if 'FULLHOUSE' in s else '_')
            poker.append(s['POKER'] if 'POKER' in s else '_')
            generala.append(s['GENERALA'] if 'GENERALA' in s else '_')
    print_scoresheet_line('4', _4)
    print_scoresheet_line('5', _5)
    print_scoresheet_line('6', _6)
    print_scoresheet_line('ESCALERA', escalera)
    print_scoresheet_line('FULLHOUSE', fullhouse)
    print_scoresheet_line('POKER', poker)
    print_scoresheet_line('GENERALA', generala)

