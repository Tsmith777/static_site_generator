import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is another text node", TextType.CODE, "http://www.vocal.com")
        node2 = TextNode("This is another text node", TextType.CODE, "http://www.vocal.com")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("scgsfgsdfgsdfgsdf", TextType.TEXT, "http://www.vocal.com")
        node2 = TextNode("This is another text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_eq3(self):
        node = TextNode("Test", TextType.TEXT,)
        node2 = TextNode("Test", TextType.TEXT,)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()