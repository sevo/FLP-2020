import unittest
import exercises as e
from functools import reduce
from operator import add


class DecoratorTests(unittest.TestCase):

    def freeze(self, *args):
        return tuple(args)


    def print_output(self, index=0):
        return e.print.__closure__[1].cell_contents[index]


    def local_variable_value(self, fct, index=0):
        return fct.__closure__[index].cell_contents


    def setUp(self):
        for _ in range(len(e.print.__closure__[1].cell_contents)):
            del e.print.__closure__[1].cell_contents[0]

    # Pomocny test, ktory zistuje ci ide vsetko tak kao ma. Toto nieje test k uloham
    def test_simple(self):
        e.simple('pokus')
        self.assertEqual(self.print_output(), self.freeze('pokus'))
        self.setUp()

        e.simple('pokus')
        e.simple('pokus2')
        self.assertEqual(self.print_output(), self.freeze('pokus'))
        self.assertEqual(self.print_output(1), self.freeze('pokus2'))


    # Uloha 1
    def test_to_be_implemented_decorator(self):
        @e.to_be_implemented_decorator
        def fct():
            pass

        fct()
        self.assertEqual(self.print_output(), self.freeze('To be implemented.'))


    # Uloha 2
    def test_starting_decorator(self):
        @e.starting_decorator
        def fct(str):
            e.print(str)

        fct('haha')
        self.assertEqual(self.print_output(), self.freeze('fct: Starting'))
        self.assertEqual(self.print_output(1), self.freeze('haha'))


    # Uloha 3
    def test_count_decorator(self):
        @e.count_decorator
        def fct():
            pass

        fct()
        self.assertEqual(self.local_variable_value(fct), 1)
        for _ in range(0, 10):
            fct()
        self.assertEqual(self.local_variable_value(fct), 11)


    # Uloha 4
    def test_memoize(self):
        def wrapper():
            counter = 0
            def fct(i):
                nonlocal counter
                counter += 1
                return i**2
            return fct

        fct = e.memoize(wrapper())
        self.assertEqual(fct(5), 25)
        self.assertEqual(self.local_variable_value(self.local_variable_value(fct, 0), 0), 1)
        for _ in range(10):
            fct(6)
        self.assertEqual(self.local_variable_value(self.local_variable_value(fct, 0), 0), 2)


    # Uloha 5
    def test_test_array_of_positives(self):
        @e.test_array_of_positives
        def sum(array):
            return reduce(add, array)

        self.assertEqual(sum([1,2,3,4]), 10)
        with self.assertRaises(ValueError):
            sum()
        with self.assertRaises(ValueError):
            sum([-1,2,3,4])
        with self.assertRaises(ValueError):
            sum(['0',2,3,4])


# Run
if __name__ == '__main__':
    unittest.main()