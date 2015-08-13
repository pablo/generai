import os
import random
import itertools

# global helpers

def most_common(lst):
    return max(set(lst), key=lst.count)


# play rules

def generala(dice):
    return len(set(dice)) == 1

def poker(dice):
    cmc = most_common(dice)
    return dice.count(cmc) >= 4

def fullhouse(dice):
    cmc = most_common(dice)
    return dice.count(cmc) == 3 and len(set(dice)) == 2

def escalera(dice):
    s = set(dice)
    return s == {1, 2, 3, 4, 5} or s == {2, 3, 4, 5, 6} or s == {1, 3, 4, 5, 6}


# play value helpers

def poker_val(dice, bonus):
    if poker(dice):
        if bonus or generala(dice):
            return 40 + 5
        return 40
    return 0

def figura_val(figura, points):
    return lambda dice, bonus: (points + (5 if bonus else 0)) if figura(dice) else 0

def numeros_val(numero):
    return lambda dice, bonus: numero*dice.count(numero)

# random dice generation helpers

def sample_wr(population, k):
    "Chooses k random elements (with replacement) from a population"
    n = len(population)
    _random, _int = random.random, int  # speed hack
    return [_int((_random() * n)+1) for i in itertools.repeat(None, k)]

def get_random_dice(n):
    return sample_wr([1,2,3,4,5,6], n)


# play functions to use in game.py

valid_plays = {
    'GENERALA': figura_val(generala, 50),
    'POKER': poker_val,
    'FULLHOUSE': figura_val(fullhouse, 30),
    'ESCALERA': figura_val(escalera, 20),
    '4': numeros_val(4),
    '5': numeros_val(5),
    '6': numeros_val(6)
}

def valid_play(play):
    return play in valid_plays

def play_value(play, dice, bonus):
    return valid_plays[play](dice, bonus)

