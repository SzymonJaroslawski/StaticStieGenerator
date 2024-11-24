import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimeter,
)
from textnode import TextNode, TextType


class TestGenerator(unittest.TestCase):
    def test_split_nodes_delimeter_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.Normal)
        new_nodes = split_nodes_delimeter([node], "`", TextType.Code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.Normal),
                TextNode("code block", TextType.Code),
                TextNode(" word", TextType.Normal),
            ],
        )

    def test_extract_markdown_links_eq(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted, expected)

    def test_extract_markdown_images_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        extracted = extract_markdown_images(text)
        self.assertEqual(extracted, expected)
