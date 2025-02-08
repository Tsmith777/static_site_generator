import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_no_images_or_links(self):
        node = TextNode("This is a text with no links or images", TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a text with no links or images")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a text with no links or images")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_with_image(self):
        node = TextNode("Hello ![test](http://example.com/image.png) world", TextType.TEXT)
        nodes = split_nodes_image([node])
        
        self.assertEqual(len(nodes), 3)
        
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
        self.assertEqual(nodes[1].text, "test")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "http://example.com/image.png")
        
        self.assertEqual(nodes[2].text, " world")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_with_link(self):
        node = TextNode("Hello [click me](https://boot.dev) world", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "click me")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://boot.dev")
        self.assertEqual(nodes[2].text, " world")