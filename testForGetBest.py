import unittest
from getbest import getCols, findTop
# Removed extra t from StringIO
from io import StringIO

# Unit tests for the getbest.py module
class TestGetBest(unittest.TestCase):
    # Test the getCols function to ensure it correctly identifies the columns for student number and mark
    def test_getCols(self):
        f = open("bestdat0.csv", "r")
        num_col, mark_col = getCols(f)
        # Assert that the correct columns for student number and mark are identified
        self.assertEqual(num_col, 1)
        # Removed extra underscore from mark_col
        self.assertEqual(mark_col, 2)

    # Test the findTop function to ensure it correctly identifies the top student and their mark
    def test_findTop(self):
        f = open("bestdat0.csv", "r")
        num_col, mark_col = getCols(f)
        best_idx, best = findTop(f, num_col, mark_col)
        # Assert that the correct top student and their mark are identified
        # Removed extra underscore from best_idx
        self.assertEqual(best_idx, '167381')
        self.assertEqual(best, 90)

# Run the unit tests
# Removed extra colon from if __name__ statement
if __name__ == '__main__':    unittest.main()  