from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    Normal = "NormalText"
    Bold = "BoldText"
    Italic = "ItalicText"
    Code = "CodeText"
    Link = "LinkText"
    Image = "ImageText"


class TextNode(object):
    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            if (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            ):
                return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node) -> LeafNode:
        if text_node.text_type == TextType.Normal:
            return LeafNode(text_node.text)

        if text_node.text_type == TextType.Bold:
            return LeafNode(text_node.text, "b")

        if text_node.text_type == TextType.Italic:
            return LeafNode(text_node.text, "i")

        if text_node.text_type == TextType.Code:
            return LeafNode(text_node.text, "code")

        if text_node.text_type == TextType.Image:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})

        if text_node.text_type == TextType.Link:
            return LeafNode(text_node.text, "a", {"href": text_node.url})

        return LeafNode("")
