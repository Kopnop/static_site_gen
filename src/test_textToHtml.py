import unittest

from textnode import TextNode, TextType
from main import *


class TestTextToHtml(unittest.TestCase):
    def test1(self):
        node = TextNode("This is a bold text node", TextType.BOLD, "https://www.boot.dev")
        converted_node = text_node_to_html_node(node)
        self.assertTrue(converted_node.to_html(), "<b>This is a bold text node</b>")

    def test_no_node(self):
        node = TextNode("wrong Node", None)
        self.assertRaises(Exception, lambda: text_node_to_html_node(node))

    def test_link(self):
        node = TextNode("link", TextType.LINKS, "https://www.google.com")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), "<a href=\"https://www.google.com\">link</a>")


if __name__ == "__main__":
    unittest.main()