"""_summary_
    """
import unittest

from mymodule1 import add


class TestAdditionFunction(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_addition_of_integers(self):
        """_summary_
        """
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)

    def test_addition_of_floats(self):
        """_summary_
        """
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add(2.3000, 4.300), 6.6)

    def test_addition_of_strings(self):
        """_summary_
        """
        self.assertEqual(add("hello", "world"), "helloworld")

    def test_addition_of_negative_numbers(self):
        """_summary_
        """
        self.assertNotEqual(add(-2, -2), 0)


if __name__ == "__main__":
    unittest.main()
