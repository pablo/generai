import os
import random
import itertools

def sample_wr(population, k):
    "Chooses k random elements (with replacement) from a population"
    n = len(population)
    _random, _int = random.random, int  # speed hack
    return [_int(_random() * n) for i in itertools.repeat(None, k)]

def get_random_dice(n):
    return sample_wr([1,2,3,4,5,6], n)

def get_play(dice):
    pass

def embutida():
    return generala(1)

def most_common(lst):
    return max(set(lst), key=lst.count)

def generala(rolls_allowed = 3):
    rolls = 0
    cmc = 0
    held = []
    while rolls < rolls_allowed:
        d = get_random_dice(5-len(held))
        dice = d + held
        assert len(dice) == 5
        if len(set(dice)) == 1:
            return True
        else:
            cmc = most_common(dice)
            held = [cmc] * dice.count(cmc)
        rolls += 1
    return False

def poker_servido():
    return poker(1)

def poker(rolls_allowed = 3):
    rolls = 0
    cmc = 0
    held = []
    while rolls < rolls_allowed:
        d = get_random_dice(5-len(held))
        dice = d + held
        cmc = most_common(dice)
        cc = dice.count(cmc)
        assert len(dice) == 5
        if cc >= 4:
            return True
        else:
            held = [cmc] * cc
        rolls += 1
    return False


def full_servido():
    return full(1)

def full(rolls_allowed = 3):
    held = []
    rolls = 0
    while rolls < rolls_allowed:
        d = get_random_dice(5-len(held))
        dice = d + held
        assert len(dice) == 5
        cmc = most_common(dice)
        cc = dice.count(cmc)
        if cc == 3 and len(set(dice)) == 2:
            return True
        else:
            if cc >= 3:
                held = [cmc] * 3
            elif cc == 2 and len(set(dice)) == 3:
                held = ([1] * 2) + ([2] * 2)
            elif cc == 2:
                held = [cmc] * 2
            else:
                held = []
        rolls += 1
    return False

def is_escalera(dice, sin_comodin):
    s = set(dice)
    if sin_comodin:
        return s == set([0, 1, 2, 3, 4]) or s == set([1, 2, 3, 4, 5])
    else:
        return s == set([0, 1, 2, 3, 4]) or s == set([1, 2, 3, 4, 5]) or s == set([2, 3, 4, 5, 0])

def escalera_sc():
    return escalera(3, True)

def escalera_sc_servida():
    return escalera(1, True)

def escalera_servida(sin_comodin = False):
    return escalera(1, sin_comodin)

def escalera(rolls_allowed = 3, sin_comodin = False):
    held = []
    rolls = 0
    while rolls < rolls_allowed:
        d = get_random_dice(5-len(held))
        dice = d + held
        assert len(dice) == 5
        if is_escalera(dice, sin_comodin):
            return True
        else:
            dif = len(set(dice))
            held = range(dif)
        rolls += 1
    return False


def sim(n, f):
    ocurrences = 0
    for i in range(n):
	if f():
	    ocurrences += 1
    return ocurrences


TOTAL = int(raw_input('cuantas simulaciones? '))

simulaciones = {
    'EMBUTIDA': embutida,
    'GENERALA': generala,
    'POKER': poker,
    'POKER SERVIDO': poker_servido,
    'FULLHOUSE SERVIDO': full_servido,
    'FULLHOUSE': full,
    'ESCALERA': escalera,
    'ESCALERA SERVIDA': escalera_servida,
    'ESCALERA SIN COMODIN': escalera_sc,
    'ESCALERA SIN COMODIN SERVIDA': escalera_sc_servida

}

for k, v in simulaciones.items():
    count = sim(TOTAL, v)
    print("{0} simulaciones {1} {2} {3}%".format(TOTAL, count, k, 100.0*float(count)/TOTAL))

raw_input('listo')
