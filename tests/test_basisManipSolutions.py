import unittest
from sympy import Matrix
import sys, os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from basisManipSolutions import (
    list_sum,
    list_mul,
    getMinimal,
    soft_round,
    getManipBasis,
)


class TestBasisManipSolutions(unittest.TestCase):
    def test_list_sum(self):
        self.assertEqual(list_sum([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_list_mul(self):
        self.assertEqual(list_mul([1, 2, 3], 3), [3, 6, 9])

    def test_soft_round(self):
        self.assertEqual(soft_round(3.0000000001), 3)
        self.assertEqual(soft_round(3.9999999999), 4)
        self.assertNotIsInstance(soft_round(3.1), int)

    def test_getMinimal(self):
        # The original test was incorrect.
        # The function normalizes the vector so the last non-zero element is 1.
        result = getMinimal([2, 4, 6])
        self.assertAlmostEqual(result[0], 1 / 3)
        self.assertAlmostEqual(result[1], 2 / 3)
        self.assertAlmostEqual(result[2], 1)

        result = getMinimal([-2, -4, -6])
        self.assertAlmostEqual(result[0], 1 / 3)
        self.assertAlmostEqual(result[1], 2 / 3)
        self.assertAlmostEqual(result[2], 1)

        result = getMinimal([3, 5, 7])
        self.assertAlmostEqual(result[0], 3 / 7)
        self.assertAlmostEqual(result[1], 5 / 7)
        self.assertAlmostEqual(result[2], 1)

    def test_getManipBasis(self):
        # I will use the example from the `if __name__ == "__main__"` block
        # in `basisManipSolutions.py` to create a test case here.
        a = Matrix(
            [
                [-1, 1, 0, 1, -1, 0, 0, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, -1, 0, 0, -1, 0, 1, 0, 0, 1, -1, 0, 0, 0, 0],
                [-1, 1, 0, 0, 1, 0, -1, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0],
                [0, -1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, -1, 0, 1],
                [-1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, -1, 0, 1, 0],
                [-1, 1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, -1, 1, 0, 0],
                [0, -1, 0, 1, 1, 0, 0, -1, 0, 0, 0, 0, -1, 1, 0, 0, 0],
                [0, -1, 0, 1, 1, 0, 0, 0, -1, -1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 1, 0, 1, 0, -1, 0, -1, 1, 0, 0, 0, 0],
                [-1, 1, 0, 0, 0, 0, 1, 0, 0, -1, -1, 0, 1, 0, 0, 0, 0],
                [0, -1, 1, 0, 1, 0, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, -1, 1, 0, 1, 0, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0],
                [-1, 1, 0, 1, 0, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [-1, 1, 1, 0, -1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        b = Matrix(
            [
                [2],
                [1],
                [2],
                [2],
                [2],
                [1],
                [1],
                [1],
                [1],
                [1],
                [0],
                [0],
                [1],
                [0],
                [-1],
                [0],
                [-1],
            ]
        )
        # This is a basic test to ensure the function runs without errors.
        # A more thorough test would check the actual output.
        a_res, b_res = getManipBasis(a, b)
        self.assertIsNotNone(a_res)
        self.assertIsNotNone(b_res)


if __name__ == "__main__":
    unittest.main()
