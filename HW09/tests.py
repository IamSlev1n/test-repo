import unittest
from homework_9 import fib_num_gen, fib_num_recursion


class FibonacciTest(unittest.TestCase):
    def test_fib_num_gen(self):
        result = list(fib_num_gen(6))
        self.assertEqual(result, [1, 1, 2, 3, 5, 8])
        with self.assertRaises(ValueError):
            list(fib_num_gen(0))

    def test_fib_num_recursion(self):
        result = fib_num_recursion(6)
        self.assertEqual(result, 8)
        with self.assertRaises(ValueError):
            fib_num_recursion(-1)
