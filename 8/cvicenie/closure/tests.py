import unittest
import exercises as e
import types

class ClosureTest(unittest.TestCase):
    # Uloha 1
    def test_nested_square(self):
        self.assertIsInstance(e.nested_square(), types.FunctionType)
        fct = e.nested_square()
        self.assertEqual(fct(5), 25)


    # Uloha 2
    def test_make_power(self):
        self.assertIsInstance(e.make_power(2), types.FunctionType)
        self.assertEqual(e.make_power(2)(5), 25)
        self.assertEqual(e.make_power(3)(5), 125)


    # Uloha 3
    def test_make_counter(self):
        counter = e.make_counter()
        self.assertEqual(counter(), 1)
        self.assertEqual(counter(), 2)
        self.assertEqual(counter(), 3)
        counter2 = e.make_counter()
        self.assertEqual(counter2(), 1)
        self.assertEqual(counter2(), 2)
        self.assertEqual(counter(), 4)