#!/usr/bin/env python3

"""Unittests for client.py to ensure that the GithubOrgClient class
works as expected.
Also decorate the test class with the parameterized decorator
to test multiple cases.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test the org method.
        """
        # Create an instance of GithubOrgClient with the specified org_name
        client = GithubOrgClient(org_name)

        org_data = client.org  # Call the org method
        # Assert that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert that org_data is correct
        # (for simplicity, we'll just assert it's not None)
        self.assertIsNotNone(org_data)


if __name__ == '__main__':
    unittest.main()
