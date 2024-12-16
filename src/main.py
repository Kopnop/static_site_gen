import shutil
import os

from textnode import *
from htmlnode import *
from splitdelimiter import *
from block_markdown import *
from generate_website import *

def main():
    copy_to_dir("/home/kopnop/workspace/github.com/kopnop/static_site_gen/static", "/home/kopnop/workspace/github.com/kopnop/static_site_gen/public/")
    # generate_page("/home/kopnop/workspace/github.com/kopnop/static_site_gen/content/index.md", 
    #                 "/home/kopnop/workspace/github.com/kopnop/static_site_gen/template.html",
    #                 "/home/kopnop/workspace/github.com/kopnop/static_site_gen/public"
    #               )
    generate_pages_recursive("/home/kopnop/workspace/github.com/kopnop/static_site_gen/content/",
                                "/home/kopnop/workspace/github.com/kopnop/static_site_gen/template.html",
                                "/home/kopnop/workspace/github.com/kopnop/static_site_gen/public"
                            )
    pass

main()