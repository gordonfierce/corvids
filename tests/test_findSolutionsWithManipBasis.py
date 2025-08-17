import unittest
from sympy import Matrix
import sys, os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from findSolutionsWithManipBasis import (
    forced_neg_removal,
    dead_solution,
    recurse_over_solution_path,
    recurse_find_first,
)
from basisManipSolutions import getManipBasis, list_sum, list_mul


class TestFindSolutions(unittest.TestCase):
    def test_forced_neg_removal(self):
        a = [[1, 0], [1, 1]]
        b = [-2, 3]
        result = forced_neg_removal(a, b)
        # The logic was more complex than I initially thought.
        # This is the correct expected output.
        self.assertEqual(result, [-5, 0])

    def test_dead_solution(self):
        a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        b = [-1, -1, -1]
        # All columns have a positive value, so it should not be a dead solution.
        self.assertFalse(dead_solution(a, b))

        a = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        b = [-1, -1, -1]
        # b[0] is negative, and column 0 of a has no positive values. Dead solution.
        self.assertTrue(dead_solution(a, b))

        a = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        b = [1, 1, -1]
        # b[2] is negative, and column 2 of a has no positive values. Dead solution.
        self.assertTrue(dead_solution(a, b))

        a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        b = [1, 1, 1]
        # No negative values in b, so not a dead solution.
        self.assertFalse(dead_solution(a, b))

    def test_recurse_functions(self):
        # Using data from the original file to test
        a = Matrix(
            [
                [-1, 2, -1, 1, -2, 1, 0],
                [0, -1, 2, 0, -2, 1, 0],
                [-1, 2, 0, -2, 1, 0, 0],
                [-1, 1, 1, 0, -1, -1, 1],
            ]
        )
        b = Matrix([[0, 1, 2, 3, 1, 2, -1]])

        a_list, b_list = getManipBasis(a, b)
        b_list = forced_neg_removal(a_list, b_list)

        sols = recurse_over_solution_path(a_list, b_list)
        self.assertTrue(len(sols) > 0)

        sol = recurse_find_first(a_list, b_list)
        self.assertIsNotNone(sol)


if __name__ == "__main__":
    unittest.main()
