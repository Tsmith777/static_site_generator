import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_text_type(self):
        text_node = TextNode("Hello World", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        expected = LeafNode(None, "Hello World")
        self.assertEqual(html_node, expected)

    def test_bold_text_type(self):
        bold_node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(bold_node)
        expected = LeafNode("b", "Bold Text")
        self.assertEqual(html_node, expected)

    def test_italic_text_type(self):
        italic_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(italic_node)
        expected = LeafNode("i", "Italic Text")
        self.assertEqual(html_node, expected)

    def test_code_text_type(self):
        code_node = TextNode("Code Text", TextType.CODE)
        html_node = text_node_to_html_node(code_node)
        expected = LeafNode("code", "Code Text")
        self.assertEqual(html_node, expected)

    def test_link_text_type(self):
        link_node = TextNode("Link Text", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(link_node)
        expected = LeafNode("a", "Link Text", {"href": "https://boot.dev"})
        self.assertEqual(html_node, expected)

    def test_image_text_type(self):
        image_node = TextNode("Image Text", TextType.IMAGE, "https://boot.dev")
        html_node = text_node_to_html_node(image_node)
        expected = LeafNode("img", "", {"src": "https://boot.dev", "alt": "Image Text"})
        self.assertEqual(html_node, expected)

    def test_bad_text_type(self):
        text_node = TextNode("Text", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
