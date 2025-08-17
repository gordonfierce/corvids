import unittest
import sys, os
from collections import defaultdict

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from RecreateData import RecreateData


class TestRecreateData(unittest.TestCase):
    def test_recreateData_simple(self):
        rd = RecreateData(
            min_score=1,
            max_score=2,
            num_samples=2,
            mean=1.5,
            variance=0.5,
            debug=False,
        )
        rd.recreateData(multiprocess=False)
        self.assertIsNotNone(rd.sols)
        # The key for sols is a tuple of (mean, variance)
        sol_key = (1.5, 0.5)
        self.assertIn(sol_key, rd.sols)
        self.assertEqual(rd.sols[sol_key], [[1, 1]])


if __name__ == "__main__":
    unittest.main()
