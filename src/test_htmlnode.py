import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HTMLNode("h1", "this is a headline", None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(html_node.__repr__(), 
                         "HTMLNode(tag: h1, value: this is a headline, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'})"
                         )

    def test_props_to_html(self):
        html_node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(html_node.props_to_html(),  " href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html2(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(),  "")

    def test_leaf_to_html(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html2(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaf_to_html3(self):
        leaf_node = LeafNode(None, "only has value")
        self.assertEqual(leaf_node.to_html(), "only has value")

    def test_parent_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html2(self):
        node = ParentNode("span", [LeafNode("b", "bold text"), LeafNode("i", "italic text")])
        node2 = ParentNode("h1", [LeafNode(None, "first leaf"), node, LeafNode("p", "second leaf")])
        self.assertEqual(node2.to_html(), "<h1>first leaf<span><b>bold text</b><i>italic text</i></span><p>second leaf</p></h1>")

    def test_parent_to_html3(self):
        node = ParentNode("b", None)
        self.assertRaises(ValueError, lambda: node.to_html())


if __name__ == "__main__":
    unittest.main()