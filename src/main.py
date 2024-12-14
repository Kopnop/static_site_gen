from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("ERROR: not a valid text type")


def main():
    #node = TextNode("This is a bold text node", TextType.BOLD, "https://www.boot.dev")
    #converted_node = text_node_to_html_node(node)
    #print(converted_node)
    # print(node)

    # html_node = HTMLNode("h1", "this is a headline", None, {
    #                                                             "href": "https://www.google.com", 
    #                                                             "target": "_blank",
    #                                                         })
    # print(html_node)
    # print(html_node.props_to_html())

    # leaf_node1 = LeafNode("p", "This is a paragraph of text.")
    # leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(leaf_node1.to_html())
    # print(leaf_node2.to_html())
    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )

    # print(node.to_html())
    pass

main()