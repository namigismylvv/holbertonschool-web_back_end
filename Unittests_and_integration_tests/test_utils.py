#!/usr/bin/env python3
"""Tests for the utils module."""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map method."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """Test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path_map),
                         result_expec)

    @parameterized.expand([
        ({}, ("a",), "KeyError('a')"),
        ({"a": 1}, ("a", "b"), "KeyError('b')")
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, error_message):
        """Test that KeyError is raised properly"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception),
                         error_message.split('(')[1][:-1])


class TestGetJson(unittest.TestCase):
    """Tests for the get_json method."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, result_expec):
        """Test get_json method"""

        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = result_expec
            self.assertEqual(get_json(test_url), result_expec)
            mock_request.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        """Test that memoization works as expected."""
        class TestClass:
            """Test class for memoize decorator."""
            def a_method(self):
                """A method that returns 42."""
                return 42

            @memoize
            def a_property(self):
                """A property that returns a value from a method."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_instance = TestClass()

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Verify results and that a_method was called only once
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
