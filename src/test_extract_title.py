import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# This is a normal Title"), "This is a normal Title")

    def test_non_title(self):
        # Test "##"
        test_title = "## This is a not a Title"
        with self.assertRaises(Exception):
            extract_title(test_title)
        
        # test no text after "#"
        test_title1 = "#"
        test_title2 = "# "
        with self.assertRaises(Exception):
            extract_title(test_title1)
        
        with self.assertRaises(Exception):
            extract_title(test_title2)

        # test no space between "#" and content
        test_title = "#hashtag"
        with self.assertRaises(Exception):
            extract_title(test_title)

if __name__ == "__main__":
    unittest.main()