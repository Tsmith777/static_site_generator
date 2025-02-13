import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_code_block(self):
        markdown_block = "``` This is a code block ```"
        self.assertEqual(block_to_block_type(markdown_block), "code")

    def test_unclosed_code_block(self):
        markdown_block = "``` This is a bad code block "
        self.assertEqual(block_to_block_type(markdown_block), "paragraph")

    def test_heading_block(self):
        markdown_block = "### This is a heading block"
        self.assertEqual(block_to_block_type(markdown_block), "heading")

    def test_quote_block(self):
        markdown_block = """>This is a quote
>Every
>Single
>line
>starts
>with
>\">\""""
        self.assertEqual(block_to_block_type(markdown_block), "quote")

    def test_bad_quote_block(self):
        markdown_block = """>This is a quote
>Every
Single
>line
>starts
>with
>\">\""""
        self.assertEqual(block_to_block_type(markdown_block), "paragraph")

    def test_unordered_list(self):
        # Basic test with single marker type
        self.assertEqual(
            block_to_block_type("* First\n* Second\n* Third"),
            "unordered_list"
        )

        # Test with mixed markers
        self.assertEqual(
            block_to_block_type("* First\n- Second\n* Third"),
            "unordered_list"
        )

        # Test with invalid lines (should return paragraph)
        self.assertEqual(
            block_to_block_type("* First\nSecond\n* Third"),
            "paragraph"
        )

        # Test with empty lines
        self.assertEqual(
            block_to_block_type("* First\n\n* Third"),
            "paragraph"
        )

    def test_edge_cases_unordered_list(self):
        # Test with just a single item
        self.assertEqual(
            block_to_block_type("* Single item"),
            "unordered_list"
        )
        
        # Test with extra spaces (should pass!)
        self.assertEqual(
            block_to_block_type("*     Extra spaces"),
            "unordered_list"
        )
        
        # Test with invalid marker (should be paragraph)
        self.assertEqual(
            block_to_block_type("*No space after asterisk"),
            "paragraph"
        )

    def test_ordered_list(self):
        # Basic test
        self.assertEqual(
            block_to_block_type("1. one\n2. two\n3. three"),
            "ordered_list"
        )

        # Test missing number
        self.assertEqual(
            block_to_block_type("1. one\n two\n3. three"),
            "paragraph"
        )

        # Test out of order numbers
        self.assertEqual(
            block_to_block_type("1. one\n3. two\n2. three"),
            "paragraph"
        )

        #Test no spaces
        self.assertEqual(
            block_to_block_type("1.one\n2.two\n3.three"),
            "paragraph"
        )

        # Test starting with wrong number
        self.assertEqual(
            block_to_block_type("2. first\n3. second"),
            "paragraph"
        )

        # Test with single item
        self.assertEqual(
            block_to_block_type("1. only item"),
            "ordered_list"
        )

        # Test with extra spaces
        self.assertEqual(
            block_to_block_type("1.  two spaces\n2.  two spaces"),
            "ordered_list"
        )