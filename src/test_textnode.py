import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()