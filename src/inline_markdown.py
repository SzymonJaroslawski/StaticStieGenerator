import re
from textnode import TextNode, TextType


def extract_title(markdown: str):
    splited = markdown.split("\n")
    if not splited[0].startswith("#") or splited[0].startswith(
        ("##", "###", "####", "#####", "######")
    ):
        raise Exception("Markdown document should start with 1 (one) #")
    return splited[0][2:]


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.Normal)]
    nodes = split_nodes_delimeter(nodes, "**", TextType.Bold)
    nodes = split_nodes_delimeter(nodes, "*", TextType.Italic)
    nodes = split_nodes_delimeter(nodes, "`", TextType.Code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Normal:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.Normal))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.Image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.Normal))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.Normal:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.Normal))
            new_nodes.append(TextNode(link[0], TextType.Link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.Normal))
    return new_nodes


def extract_markdown_links(text) -> list:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_images(text) -> list:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
