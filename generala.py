import os
import random
import itertools

# common helpers

# play rules

def generala(dice):
    return len(set(dice)) == 1

def poker(dice):
    pass


# play value helpers

def figura_val(figura, points):
    return lambda dice, bonus: (points + (5 if bonus else 0)) if figura(dice) else 0

def numeros_val(numero):
    return lambda dice, bonus: numero*dice.count(numero)

# random dice generation helpers

def sample_wr(population, k):
    "Chooses k random elements (with replacement) from a population"
    n = len(population)
    _random, _int = random.random, int  # speed hack
    return [_int(_random() * n) for i in itertools.repeat(None, k)]

def get_random_dice(n):
    return sample_wr([1,2,3,4,5,6], n)


# play functions to use in game.py

valid_plays = {
    'GENERALA': figura_val(generala, 50),
    'POKER': figura_val(poker, 40),
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

