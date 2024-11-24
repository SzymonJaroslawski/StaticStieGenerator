import re
from textnode import TextNode, TextType


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = list()
    for old_node in old_nodes:
        if old_node.text_type != TextType.Normal:
            new_nodes.append(old_node)
            continue
        split_nodes = list()
        sections = old_node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.Normal))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def extract_markdown_links(text) -> list:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_images(text) -> list:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
