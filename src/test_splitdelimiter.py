import unittest

from textnode import *
from splitdelimiter import *

class TestSplitDelimiter(unittest.TestCase):

    def test(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        correct_nodes = [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        for i in range(len(correct_nodes)):
            self.assertEqual(correct_nodes[i], new_nodes[i])

    def test_block_at_end(self):
        node = TextNode("at the end is a `code block`", TextType.TEXT)
        correct_nodes = [
                            TextNode("at the end is a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        for i in range(len(correct_nodes)):
            self.assertEqual(correct_nodes[i], new_nodes[i])       

    def test_bold(self):
        node = TextNode("here is **bold** text", TextType.TEXT)
        correct_nodes = [
                            TextNode("here is ", TextType.TEXT),
                            TextNode("bold", TextType.BOLD),
                            TextNode(" text", TextType.TEXT),
                        ]
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        for i in range(len(correct_nodes)):
            self.assertEqual(correct_nodes[i], new_nodes[i])

    def test_wrong_syntax(self):
        node = TextNode("here * is * a Error * correct?", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "*", TextType.BOLD))
        #print(2)

    #regex tests
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        new_text = extract_markdown_images(text)                
        correct_text = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(new_text, correct_text)

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        new_text = extract_markdown_links(text)
        correct_text = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(new_text, correct_text)

    #split node tests
    def test_split_link_at_end(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )  
        new_nodes = split_nodes_links([node])
        correct_nodes = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                        ]
        self.assertEqual(new_nodes, correct_nodes)

    def test_split_link_at_begin(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )  
        new_nodes = split_nodes_links([node])
        correct_nodes = [
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                        ]
        self.assertEqual(new_nodes, correct_nodes) 

    def test_split_link_in_middle(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) the end",
            TextType.TEXT,
        )  
        new_nodes = split_nodes_links([node])
        correct_nodes = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                        TextNode(" the end", TextType.TEXT),
                        ]
        self.assertEqual(new_nodes, correct_nodes)   
    
    def test_split_link_no_link(self):
        node = TextNode("no link here", TextType.TEXT)
        new_nodes = split_nodes_links([node]) 
        self.assertEqual(new_nodes, [node]) 

    def test_split_link_only_links(self):
        node = TextNode("[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        correct_nodes = [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                         TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(new_nodes, correct_nodes)

    def test_split_images(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        correct_nodes = [
                        TextNode("This is text with a ", TextType.TEXT),
                        TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        ]
        self.assertEqual(new_nodes, correct_nodes)

    #test text to text nodes
    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_text = text_to_textnodes(text)
        correct_text = [
                        TextNode("This is ", TextType.TEXT),
                        TextNode("text", TextType.BOLD),
                        TextNode(" with an ", TextType.TEXT),
                        TextNode("italic", TextType.ITALIC),
                        TextNode(" word and a ", TextType.TEXT),
                        TextNode("code block", TextType.CODE),
                        TextNode(" and an ", TextType.TEXT),
                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", TextType.TEXT),
                        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(new_text, correct_text)

    def test_text_to_text_nodes_multiple_bold(self):
        text = "**this** text has **many bold** words"
        new_text = text_to_textnodes(text)
        correct_text = [TextNode("this", TextType.BOLD),
                        TextNode(" text has ", TextType.TEXT),
                        TextNode("many bold", TextType.BOLD),
                        TextNode(" words", TextType.TEXT),
        ]
        self.assertEqual(new_text, correct_text)


if __name__ == "__main__":
    unittest.main()