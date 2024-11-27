import os
import pathlib

from blocks import markdown_to_html_node
from inline_markdown import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str):
    if not os.path.exists(from_path) or not os.path.exists(template_path):
        raise Exception("Provided path does not exist")
    dest_path = dest_path.replace(".md", ".html")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    path_to_create = os.path.split(dest_path)[0]
    print(f"Creating dir {path_to_create}")
    pathlib.Path(path_to_create).mkdir(parents=True, exist_ok=True)
    f = open(from_path)
    f_content = f.read()
    t = open(template_path)
    t_content = t.read()
    title = extract_title(f_content)
    html = markdown_to_html_node(f_content).to_html()
    t_content = t_content.replace("{{ Title }}", title)
    t_content = t_content.replace("{{ Content }}", html)
    d = open(dest_path, "w+")
    d.write(t_content)


def generate_page_recursive(base_path, dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content) or not os.path.exists(template_path):
        raise Exception("Provided path does not exist")
    files = os.scandir(dir_path_content)
    for file in files:
        if file.is_file():
            if os.path.splitext(file.path)[1] == ".md":
                generate_page(
                    file.path,
                    template_path,
                    file.path.replace(base_path, dest_dir_path),
                )
        elif file.is_dir():
            generate_page_recursive(base_path, file.path, template_path, dest_dir_path)
