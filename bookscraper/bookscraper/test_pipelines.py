"""This module provides classes and methods for setting up and running test cases. 
It allows you to define test classes, test methods, and assertions to verify that your code is working as expected."""
import unittest
"""The Mock class from the unittest.mock module is used to create mock objects. 
Mock objects mimic the behavior of real objects but allow you to control and inspect their interactions during testing.
The patch function from the unittest.mock module is used to temporarily modify or replace objects in a way that's 
transparent to the code being tested. """
from unittest.mock import Mock, patch

from pipelines import BookscraperPipeline, SaveToMySQLPipeline

class TestBookscraperPipeline(unittest.TestCase):

    def test_process_item(self):
        # Create a mock item and spider
        mock_item = {
            "title": "Sample Book",
            "price": "£10.99",
            "availability": "In stock (5 available)",
    
        }
        mock_spider = Mock()

        # Instantiate the pipeline
        pipeline = BookscraperPipeline()

        # Call process_item
        result = pipeline.process_item(mock_item, mock_spider)

        # Verify that the item has been processed correctly
        self.assertEqual(result["title"], "Sample Book")
        self.assertEqual(result["price"], 10.99)
        self.assertEqual(result["availability"], 5)


class TestSaveToMySQLPipeline(unittest.TestCase):

    @patch('your_module.mysql.connector.connect')
    def setUp(self, mock_connect):
        self.pipeline = SaveToMySQLPipeline()
        self.mock_conn = mock_connect.return_value
        self.mock_cursor = self.mock_conn.cursor.return_value

    def test_process_item(self):
        mock_item = {
            "url": "http://example.com",
            "title": "Sample Book",
            "price": 10.99,
            "availability": 5,
    
        }
        mock_spider = Mock()

        # Call process_item
        self.pipeline.process_item(mock_item, mock_spider)

        # Verify that the insert statement was executed
        self.assertTrue(self.mock_cursor.execute.called)
        # Verify that the commit was called
        self.assertTrue(self.mock_conn.commit.called)

    def test_close_spider(self):
        mock_spider = Mock()

        # Call close_spider
        self.pipeline.close_spider(mock_spider)

        # Verify that the cursor and connection were closed
        self.assertTrue(self.mock_cursor.close.called)
        self.assertTrue(self.mock_conn.close.called)

if __name__ == '__main__':
    unittest.main()
