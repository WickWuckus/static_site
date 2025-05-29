import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        html = HTMLNode(
            "a", 
            "Test Link", 
            None, 
            {"href": "https://www.google.com", "target": "_blank",}
            )
        html2 = HTMLNode(
            "a", 
            "Test Link", 
            None, 
            {}
            )
        expected_result = ' href="https://www.google.com" target="_blank"'
        expected_result2 = ''
        result = html.props_to_html()
        result2 = html2.props_to_html()
        self.assertEqual(result, expected_result)
        self.assertEqual(result2, expected_result2)
    def test_props_to_html_none(self):
        html = HTMLNode(
            "a", 
            "Test Link", 
            None, 
            None
            )
        expected_result = ''
        result = html.props_to_html()
        self.assertEqual(result, expected_result)
    def test_to_html(self):
        html = HTMLNode(
            "a", 
            "Test Link", 
            None, 
            None
            )
        with self.assertRaises(NotImplementedError):
            html.to_html()
        


if __name__ == "__main__":
    unittest.main()