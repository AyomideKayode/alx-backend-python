#!/usr/bin/env python3

"""Unittests for utils.py to ensure that the access_nested_map function
works as expected.
Also decorate the test class with the parameterized decorator
to test multiple cases.
"""

import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b')
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_message, expected_key):
        with self.assertRaises(expected_message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class to test the get_json function.
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test the get_json function returns the expected result.
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
