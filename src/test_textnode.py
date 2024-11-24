import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node", TextType.Bold)
        node2 = TextNode("This is text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is text node with url", TextType.Bold, "www.boot.dev")
        node2 = TextNode("This is text node", TextType.Bold)
        self.assertNotEqual(node, node2)

    def test_text_to_leaf(self):
        nodeNormal = TextNode("Normal text", TextType.Normal).text_node_to_html_node()
        leafNormal = LeafNode("Normal text")
        self.assertEqual(nodeNormal, leafNormal)
        nodeBold = TextNode("Bold text", TextType.Bold).text_node_to_html_node()
        leafBold = LeafNode("Bold text", "b")
        self.assertEqual(nodeBold, leafBold)
        nodeItalic = TextNode("Italic text", TextType.Italic).text_node_to_html_node()
        leafItalic = LeafNode("Italic text", "i")
        self.assertEqual(nodeItalic, leafItalic)
        nodeCode = TextNode("Code text", TextType.Code).text_node_to_html_node()
        leafCode = LeafNode("Code text", "code")
        self.assertEqual(nodeCode, leafCode)
        nodeLink = TextNode(
            "Link text", TextType.Link, "www.google.com"
        ).text_node_to_html_node()
        leafLink = LeafNode("Link text", "a", {"href": "www.google.com"})
        self.assertEqual(nodeLink, leafLink)
        nodeImage = TextNode(
            "Image text", TextType.Image, "www.google.com"
        ).text_node_to_html_node()
        leafImage = LeafNode("", "img", {"src": "www.google.com", "alt": "Image text"})
        self.assertEqual(nodeImage, leafImage)


if __name__ == "__main__":
    unittest.main()
