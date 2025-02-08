import unittest
from extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    # Basic Cases
    def test_basic_image(self):
        text = "![alt text](https://example.com/img.jpg)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://example.com/img.jpg")])

    def test_basic_link(self):
        text = "[link text](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [("link text", "https://example.com")])
    
    def test_multiple_images(self):
        text = "Please look at this image: ![alt text](https://example.com/img.jpg), and also this one: ![alt text 2](https://example2.com/img.jpg)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://example.com/img.jpg"),("alt text 2", "https://example2.com/img.jpg")])

    def test_multiple_links(self):
        text = "[link text](https://example.com) and [link text 2](https://example2.com)"
        self.assertEqual(extract_markdown_links(text), [("link text", "https://example.com"),("link text 2", "https://example2.com")])

    def test_mix_of_images_and_links1(self):
        text = "[link text](https://example.com) and ![alt text](https://example.com/img.jpg)"
        self.assertEqual(extract_markdown_links(text), [("link text", "https://example.com")])

    def test_mix_of_images_and_links2(self):
        text = "[link text](https://example.com) and ![alt text](https://example.com/img.jpg)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://example.com/img.jpg")])

    # Edge Cases
    def test_empty_alt_text(self):
        text = "![](https://example.com/img.jpg)"
        self.assertEqual(extract_markdown_images(text), [("", "https://example.com/img.jpg")])

    def test_empty_url(self):
        text = "![alt text]()"
        self.assertEqual(extract_markdown_images(text), [("alt text", "")])

    def test_no_matches(self):
        text = "This is just plain text with no markdown"
        self.assertEqual(extract_markdown_links(text), [])
        self.assertEqual(extract_markdown_images(text), [])

    def test_nested_brackets(self):
        text = "![alt [text] here](https://example.com/img.jpg)"
        self.assertEqual(extract_markdown_images(text), [("alt [text] here", "https://example.com/img.jpg")])
        
        text_link = "[link [text] here](https://example.com)"
        self.assertEqual(extract_markdown_links(text_link), [("link [text] here", "https://example.com")])

    def test_special_chars_in_url(self):
        # Test URLs with query parameters, fragments, and special characters
        text = "![alt text](https://example.com/img.jpg?size=large&format=png#header)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://example.com/img.jpg?size=large&format=png#header")])
        
        text_link = "[boot.dev](https://boot.dev/learn/learn-python?utm_source=test&page=1)"
        self.assertEqual(extract_markdown_links(text_link), [("boot.dev", "https://boot.dev/learn/learn-python?utm_source=test&page=1")])

    def test_malformed_markdown(self):
        text = "![alt text(https://example.com/img.jpg"  # missing closing bracket
        self.assertEqual(extract_markdown_images(text), [])
    
        text = "[link text] (https://example.com)"  # space between brackets and parentheses
        self.assertEqual(extract_markdown_links(text), [])
    


if __name__ == "__main__":
    unittest.main()