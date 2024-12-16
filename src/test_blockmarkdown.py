import unittest

from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    #test markdown_to_blocks
    def test_to_blocks(self):
        md = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        new_blocks = markdown_to_blocks(md)
        correct = ["# This is a heading",
                   "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                   "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(new_blocks, correct)

    def test_to_block_with_empty(self):
        new_blocks = markdown_to_blocks("")
        self.assertEqual(new_blocks, [])

    ##test block_to_block_type
    def test_to_block_type(self):
        self.assertEqual(block_to_block_type("### headline"), "heading")
        self.assertEqual(block_to_block_type("``` code block ```"), "code")
        self.assertEqual(block_to_block_type(">quote"), "quote")
        self.assertEqual(block_to_block_type("* an\n* unordered\n* list"), "unordered_list")
        self.assertEqual(block_to_block_type("1. an\n2. ordered\n3. list"), "ordered_list")
        self.assertEqual(block_to_block_type("a normal paragraph"), "paragraph")

    #test markdown_to_htmlnode
    def test_x(self):
        #text = "### heading 3\n\nthis is a **paragraph**\n\n``` code block ```\n\n* an\n* unordered\n* list\n\n1. an\n2. ordered\n3. list\n\n>quote"
        ul = "* unordered list\n* unordered with a **bold word**"
        ouput = markdown_to_html_node(ul)
        #correct_output = ParentNode("div", [ParentNode("ul", ParentNode("li", []))])
        print("\n")
        print(ouput)
    
    def test_md_to_html_wrong_syntax(self):
        self.assertRaises(Exception, lambda: markdown_to_html_node("### heading\n\n>quote **with** **bold"))

if __name__ == "__main__":
    unittest.main()