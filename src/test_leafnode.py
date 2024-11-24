import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("Test", "p")
        node2 = LeafNode("Test", "p")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = LeafNode("Test", "h")
        node2 = LeafNode("test", "p")
        self.assertNotEqual(node, node2)

    def test_to_html(self):
        node = LeafNode(
            "Click me!",
            "a",
            {
                "href": "www.google.com",
                "target": "_blank",
            },
        ).to_html()
        test_str = '<a href="www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node, test_str)


if __name__ == "__main__":
    unittest.main()
