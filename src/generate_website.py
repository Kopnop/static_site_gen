import shutil
import os

from block_markdown import *

#without using copytree()
def copy_to_dir(origin, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    origin_files_list = os.listdir(origin)
    for file in origin_files_list:
        file_path = os.path.join(origin, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination)
        else:
            new_destination_path = os.path.join(destination, file)
            os.mkdir(new_destination_path)
            copy_to_dir(file_path, new_destination_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip(" ")
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
        markdown_file.close()
    with open(template_path) as template_file:        
        template = template_file.read()
        template_file.close()
    html_nodes = markdown_to_html_node(markdown)
    #print(type(html_nodes))
    #TODO: fix "code" part
    #print(html_nodes)
    #print("\n")
    html_code = html_nodes.to_html()
    #print(html_code)
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_code)
    #print(template)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    with open((dest_path+ "/index.html"), "w") as f:
        f.write(template)
        f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    origin_files_list = os.listdir(dir_path_content)
    for file in origin_files_list:
        file_path = os.path.join(dir_path_content, file)
        if os.path.isfile(file_path):
            generate_page(file_path, template_path, dest_dir_path)
        else:
            new_destination_path = os.path.join(dest_dir_path, file)
            os.mkdir(new_destination_path)
            generate_pages_recursive(file_path, template_path, new_destination_path)
    