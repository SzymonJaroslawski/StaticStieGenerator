from enum import Enum
from inline_markdown import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode


class BlockType(Enum):
    Paragraph = "Paragraph"
    Heading = "Heading"
    Code = "Code"
    Quote = "Quote"
    UnorderedList = "UnorderedList"
    OrderedList = "OrderedList"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_blocktype(block)
    match block_type:
        case BlockType.Paragraph:
            return paragraph_to_html_node(block)
        case BlockType.Heading:
            return headding_to_html_node(block)
        case BlockType.Code:
            return code_to_html_node(block)
        case BlockType.Quote:
            return quote_to_html_node(block)
        case BlockType.UnorderedList:
            return ulist_to_html_node(block)
        case BlockType.OrderedList:
            return olist_to_html_node(block)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = TextNode.text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def headding_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def block_to_blocktype(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.Heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.Code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.Paragraph
        return BlockType.Quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.Paragraph
        return BlockType.UnorderedList
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.Paragraph
        return BlockType.UnorderedList
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.Paragraph
            i += 1
        return BlockType.OrderedList
    return BlockType.Paragraph


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
