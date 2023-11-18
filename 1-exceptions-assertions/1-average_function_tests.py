import unittest
from average_function import average

class TestAverageFunction(unittest.TestCase):
    def test_valid_input(self):
        # Test case with a valid input list
        result = average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_empty_list(self):
        # Test case with an empty input list
        with self.assertRaises(AssertionError) as context:
            average([])
        self.assertEqual(
            str(context.exception),
            "Input list must not be empty",
            "Expected AssertionError with appropriate message for empty list",
        )

    def test_single_element(self):
        # Test case with a single-element input list
        result = average([10])
        self.assertEqual(result, 10.0)

    def test_negative_numbers(self):
        # Test case with negative numbers in the input list
        result = average([-1, -2, -3, -4, -5])
        self.assertEqual(result, -3.0)

if __name__ == '__main__':
    unittest.main()
