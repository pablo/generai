import os
import random
import itertools

# rules

# common helpers

def generala(dice):
    return len(set(dice)) == 1

def poker(dice):
    pass

def sample_wr(population, k):
    "Chooses k random elements (with replacement) from a population"
    n = len(population)
    _random, _int = random.random, int  # speed hack
    return [_int(_random() * n) for i in itertools.repeat(None, k)]

def get_random_dice(n):
    return sample_wr([1,2,3,4,5,6], n)

