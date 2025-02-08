import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_valid_delimited_text(self):
        input_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)

        # Assertions
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_consecutive_delimiters(self):
        input_nodes = [TextNode("This is bold ** ** text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)

        # Assertions
        self.assertEqual(len(result), 3)  # Should split into 3 nodes
        self.assertEqual(result[0].text, "This is bold ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "")  # Empty string for consecutive delimiters
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_code_delimeters(self):
        input_nodes = [TextNode("This is `code` text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)