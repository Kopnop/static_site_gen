from textnode import *
from htmlnode import *
from splitdelimiter import *
from block_markdown import *

def main():
    #print(f"h{count_hashes("# 3#")}")
    #count_hashes("### 3#")
    quote = "### heading\n\n>quote with **bold** word"
    ul = "* an\n* undordered with a *italic looking* word\n* list"
    ol = "1. ordered\n2. **bold word**\n3. list"
    ouput = markdown_to_html_node(ol)
    print("\n")
    print(ouput)
    pass

main()