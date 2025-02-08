import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_no_tag(self):
        # test raw text with no tag
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")

    def test_leaf_node_no_value(self):
        # test ValueError is raised when no value
        node = LeafNode("h", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_with_tag(self):
        # test basic tag rendering
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_leaf_node_with_props(self):
        # test tag with properties
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://example.com\">Click me!</a>")