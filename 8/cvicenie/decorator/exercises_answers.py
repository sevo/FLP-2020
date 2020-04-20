import sys
sys.path.insert(0,'..')
from utils import *

# Uloha 1
def to_be_implemented_decorator(fct):
    def wrapper(*args, **kwargs):
        return print("To be implemented.")
    return wrapper


# Uloha 2
def starting_decorator(fct):
    def wrapper(*args, **kwargs):
        print("{}: Starting".format(fct.__name__))
        return fct(*args, **kwargs)
    return wrapper


# Uloha 3
def count_decorator(fct):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        return fct(*args, **kwargs)
    return wrapper


# Uloha 4
def memoize(f):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return wrapper


# Uloha 5
def test_array_of_positives(fct):
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            raise ValueError
        for value in args[0]:
            if type(value) != int or value <= 0:
                raise ValueError
        return fct(*args, **kwargs)
    return wrapper

