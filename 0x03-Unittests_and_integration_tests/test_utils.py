#!/usr/bin/env python3

"""Unittests for utils.py to ensure that the access_nested_map function
works as expected.
Also decorate the test class with the parameterized decorator
to test multiple cases.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test the access of nested_map.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
