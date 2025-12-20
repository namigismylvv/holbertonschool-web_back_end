#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases for GithubOrgClient class
    """
    # Declare class attributes to satisfy Pylint
    org_payload: dict
    repos_payload: list
    expected_repos: list
    apache2_repos: list

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock external requests
        """
        # Start patcher for requests.get
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect function to return appropriate responses
        def get_side_effect(url):
            """
            Side effect function to return mock responses based on URL
            """
            class MockResponse:
                """
                Mock response class with json method
                """

                def __init__(self, json_data):
                    self._json_data = json_data
                    self.status_code = 200

                def json(self):
                    """
                    Return the json data
                    """
                    return self._json_data

                def raise_for_status(self):
                    """
                    Mock the raise_for_status method of requests.Response
                    """
                    if self.status_code >= 400:
                        raise HTTPError(f"HTTP Error: {self.status_code}")

            # Return appropriate fixture based on URL
            if url.endswith('/orgs/testorg'):
                return MockResponse(cls.org_payload)
            if url.endswith('/orgs/testorg/repos'):
                return MockResponse(cls.repos_payload)
            return MockResponse({})  # Default empty response

        # Configure mock with side_effect
        cls.mock_get.side_effect = get_side_effect

        # Initialize the client
        cls.client = GithubOrgClient('testorg')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method in integration
        """
        # Call the public_repos method
        result = self.client.public_repos()

        # Assert that the result matches the expected repos from fixtures
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos method with license
        """
        # Call the public_repos method
        result = self.client.public_repos('apache-2.0')

        # Assert that the result matches the apache2_repos from fixtures
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
