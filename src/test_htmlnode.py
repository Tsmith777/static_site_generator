import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")
    def test_props_to_html2(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
    def test_props_to_html3(self):
        node = HTMLNode(props={"alt": "Description of image"})
        self.assertEqual(node.props_to_html(), " alt=\"Description of image\"")

if __name__ == "__main__":
    unittest.main()