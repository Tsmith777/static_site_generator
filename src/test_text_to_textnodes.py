import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_no_formatting(self):
        text = "This is a line with no special formatting"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a line with no special formatting")

    def test_bold(self):
        text = "This is a line with **bold** formatting"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "This is a line with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

        self.assertEqual(nodes[2].text, " formatting")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_italic(self):
        text = "This is a line with *italic* formatting"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "This is a line with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)

        self.assertEqual(nodes[2].text, " formatting")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_image(self):
        text = "This is a line with ![Google](http://www.google.com) formatting"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "This is a line with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "Google")
        self.assertEqual(nodes[1].url, "http://www.google.com")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)

        self.assertEqual(nodes[2].text, " formatting")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_link(self):
        text = "This is a line with [Google](http://www.google.com) formatting"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "This is a line with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "Google")
        self.assertEqual(nodes[1].url, "http://www.google.com")
        self.assertEqual(nodes[1].text_type, TextType.LINK)

        self.assertEqual(nodes[2].text, " formatting")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_multiple(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        self.assertEqual(len(nodes), 10)

        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)

        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE)

        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)

        self.assertEqual(nodes[7].text, "obi wan image")
        self.assertEqual(nodes[7].url, "https://i.imgur.com/fJRm4Vk.jpeg")
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)

        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[8].text_type, TextType.TEXT)

        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].url, "https://boot.dev")
        self.assertEqual(nodes[9].text_type, TextType.LINK)

    def test_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "")

if __name__ == "__main__":
    unittest.main()