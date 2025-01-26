
#!/usr/bin/python3
"""Unit Tests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit Tests for max_integer([..])."""

    def test_ordered(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_single_element(self):
        one_element = [12]
        self.assertEqual(max_integer(one_element), 12)
        
    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        floats = [2.12, 9.0, -12.4, 20.9]
        self.assertEqual(max_integer(floats), 20.9)

    def test_mixed_ints_floats(self):
        ints_and_floats = [9, 2.2, -9.9, 6]
        self.assertEqual(max_integer(ints_and_floats), 9)

    def test_string(self):
        ## returns char with highest ASCII value
        string = "String"
        self.assertEqual(max_integer(string), 't')

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)
  
    def test_list_of_strings(self):
        strings = ["This", "is", "a", "list"]
        self.assertEqual(max_integer(strings), "list")


if __name__ == '__main__':
    unittest.main()
