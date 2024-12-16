import re

from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if not delimiter in node.text:
            new_nodes.append(node)
            continue
        #     raise Exception("invalid markdown syntax: delimiter not found")
        #print(node.text)
        parts = node.text.split(delimiter)
        #print(parts)
        if len(parts) % 2 == 0:
            raise Exception("invalid markdown syntax: length")

        # if (parts[0]) != "":
        #     new_nodes.append(TextNode(parts[0], TextType.TEXT))
        # if (parts[1]) != "":
        #     new_nodes.append(TextNode(parts[1], text_type))
        # if (parts[2]) != "":
        #     new_nodes.append(TextNode(parts[2], TextType.TEXT))
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    #return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return re.findall(r"!\[([^\]]+)\]\(([^)]+)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)

def split_nodes_image(old_nodes):
        ls = []
        for node in old_nodes:
            images = extract_markdown_images(node.text)
            rest = node.text
            if not images:
                ls.append(node)
                continue

            for image in images:
                split = rest.split(f"![{image[0]}]({image[1]})" , 1)
                if split[0] != "":
                    ls.append(TextNode(split[0], TextType.TEXT))
                ls.append(TextNode(image[0], TextType.IMAGE, image[1]))
                rest = split[1]
            if rest != "":
                ls.append(TextNode(rest, TextType.TEXT))
        return ls
            

def split_nodes_links(old_nodes):
        ls = []
        for node in old_nodes:
            links = extract_markdown_links(node.text)
            rest = node.text
            if not links:
                ls.append(node)
                continue

            for link in links:
                split = rest.split(f"[{link[0]}]({link[1]})" , 1)
                if split[0] != "":
                    ls.append(TextNode(split[0], TextType.TEXT))
                ls.append(TextNode(link[0], TextType.LINK, link[1]))
                rest = split[1]
            if rest != "":
                ls.append(TextNode(rest, TextType.TEXT))
        return ls
            
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes


