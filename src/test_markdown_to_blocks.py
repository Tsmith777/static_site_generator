import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_regular_block(self):
        markdown = """# Heading

This is a paragraph
with multiple lines.

* List item 1
* List item 2"""
            
        self.assertEqual(markdown_to_blocks(markdown), 
            ["# Heading", "This is a paragraph\nwith multiple lines.", "* List item 1\n* List item 2"])
        
    def test_extra_blank_lines(self):
        markdown = """# Heading



This is a paragraph.


* List item"""

        self.assertEqual(markdown_to_blocks(markdown), 
            ["# Heading", "This is a paragraph.", "* List item"])