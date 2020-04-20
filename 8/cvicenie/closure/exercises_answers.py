# Uloha 1
def nested_square():
    def square(x):
        return x**2
    return square


# Uloha 2
def make_power(exponent):
    def power(n):
        return n**exponent
    return power


# Uloha 3
def make_counter():
    counter = 0
    def add():
        nonlocal counter
        counter += 1
        return counter
    return add


# Uloha 4
class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def add(self, value=1):
        self.value += value

    def reset(self):
        self.value = 0

def ClosureCounter(value=0):
    def add(increment=1):
        nonlocal value
        value += increment

    def reset():
        nonlocal value
        value = 0

    return {'add': add, 'reset': reset}