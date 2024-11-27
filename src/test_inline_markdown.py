import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    extract_title,
    split_nodes_delimeter,
    text_to_textnodes,
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

    def test_extract_title_eq(self):
        title = extract_title("# Hello")
        expected_title = "Hello"
        self.assertEqual(title, expected_title)

    def test_extract_title_exception(self):
        level = "#"
        for i in range(5):
            self.assertRaises(Exception, extract_title, f"{level * (i + 2)} Hello")

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

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.Normal),
            TextNode("text", TextType.Bold),
            TextNode(" with an ", TextType.Normal),
            TextNode("italic", TextType.Italic),
            TextNode(" word and a ", TextType.Normal),
            TextNode("code block", TextType.Code),
            TextNode(" and an ", TextType.Normal),
            TextNode(
                "obi wan image", TextType.Image, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.Normal),
            TextNode("link", TextType.Link, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)
