import re

from htmlnode import *
from textnode import *
from splitdelimiter import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    #print(blocks)
    ls = []
    for block in blocks:
        if block != "":    
            block.strip()        
            ls.append(block)
    return ls

def block_to_block_type(block):
    if re.search(r"^#{1,6} [^\n]+", block):
        return "heading"
    if re.search(r"```[\s\S]*?```", block):
        return "code"
    if re.search(r"^>.+", block):
        return "quote"
    if re.search(r"^[-*] .+", block):
        return "unordered_list"
    if re.search(r"^(?:\d+\.\s).+", block):
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    converted_blocks = []
    for block in md_blocks:
        match block_to_block_type(block):
            case "quote":
                text_blocks = text_to_textnodes(block[2:])
                html_nodes = []
                for text_block in text_blocks:
                    html_nodes.append(text_node_to_html_node(text_block))
                #converted_blocks.append(LeafNode("blockquote", block[1:]))
                converted_blocks.append(ParentNode("blockquote", html_nodes))
            case "unordered_list":
                list_items = block.split("\n")
                list_nodes = []
                for item in list_items:
                    #item[2:] to ignore "* "
                    text_blocks = text_to_textnodes(item[2:])
                    html_nodes = []
                    for text_block in text_blocks:
                        html_nodes.append(text_node_to_html_node(text_block))
                    list_nodes.append(ParentNode("li", html_nodes))
                parent = ParentNode("ul", list_nodes)
                converted_blocks.append(parent)
            case "ordered_list":
                list_items = block.split("\n")
                list_nodes = []
                for item in list_items:
                    #item[2:] to ignore "* "
                    text_blocks = text_to_textnodes(item[3:])
                    html_nodes = []
                    for text_block in text_blocks:
                        html_nodes.append(text_node_to_html_node(text_block))
                    list_nodes.append(ParentNode("li", html_nodes))
                parent = ParentNode("ol", list_nodes)
                converted_blocks.append(parent)
            case "code":
                text_blocks = text_to_textnodes(block[4:-3])
                html_nodes = []
                for text_block in text_blocks:
                    html_nodes.append(text_node_to_html_node(text_block))

                code_node = ParentNode("code", html_nodes)
                #TODO: check if list needed
                parent = ParentNode("pre", [code_node])
                converted_blocks.append(parent)
            case "heading":
                amount_hashes = count_hashes(block)
                if amount_hashes > 6:
                    raise ValueError("too many # in heading")

                text_blocks = text_to_textnodes(block[amount_hashes+1:])
                html_nodes = []
                for text_block in text_blocks:
                    html_nodes.append(text_node_to_html_node(text_block))
                
                converted_blocks.append(ParentNode(f"h{amount_hashes}", html_nodes))
            case "paragraph":
                #handle_paragraphs(block)
                text_blocks = text_to_textnodes(block)
                html_nodes = []
                for text_block in text_blocks:
                    html_nodes.append(text_node_to_html_node(text_block))
                converted_blocks.append(ParentNode("p", html_nodes))
    return ParentNode("div", converted_blocks)
            

def count_hashes(text):
    match = re.match(r"^#+", text)
    if not match:
        raise ValueError("ERROR: no # found in heading")
    return len(match.group())

def text_to_children(text):
    pass