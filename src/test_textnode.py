import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node1 = TextNode("test", "bold", "url")
        node2 = TextNode("test", "bold", "url")
        self.assertEqual(node1, node2)

    def test_eq3(self):
        node1 = TextNode("test", "bold")
        node2 = TextNode("test", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)

    #text_node_to_html_node tests
    def test1(self):
        node = TextNode("This is a bold text node", TextType.BOLD, "https://www.boot.dev")
        converted_node = text_node_to_html_node(node)
        self.assertTrue(converted_node.to_html(), "<b>This is a bold text node</b>")

    def test_no_node(self):
        node = TextNode("wrong Node", None)
        self.assertRaises(Exception, lambda: text_node_to_html_node(node))

    def test_link(self):
        node = TextNode("link", TextType.LINK, "https://www.google.com")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), "<a href=\"https://www.google.com\">link</a>")


if __name__ == "__main__":
    unittest.main()