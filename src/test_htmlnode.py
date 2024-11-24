import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "a",
            "google it",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = node = HTMLNode(
            "a",
            "google it",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNode(
            "a",
            "google it",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            "div",
            "google it",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "google it",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        ).props_to_html()
        props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node, props)


if __name__ == "__main__":
    unittest.main()
