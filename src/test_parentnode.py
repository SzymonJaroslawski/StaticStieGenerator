import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("Italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("Italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("Italic text", "i"),
                LeafNode("Normal text", None),
            ],
        ).to_html()
        test_str = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node, test_str)

    def test_nested_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                ParentNode(
                    "p",
                    [
                        LeafNode("Bold text", "b"),
                        ParentNode(
                            "p",
                            [LeafNode("Normal text", None), LeafNode("Bold text", "b")],
                        ),
                    ],
                ),
                LeafNode("Normal text", None),
            ],
        ).to_html()
        test_str = "<p><b>Bold text</b>Normal text<p><b>Bold text</b><p>Normal text<b>Bold text</b></p></p>Normal text</p>"
        self.assertEqual(node, test_str)
