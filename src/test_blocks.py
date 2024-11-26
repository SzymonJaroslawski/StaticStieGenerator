import unittest

from blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_blocktype,
    markdown_to_html_node,
)


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks_eq(self):
        markdown_file = open(
            r"/home/szymon/Programowanie/StaticStieGenerator/content/test.md"
        )
        markdown = markdown_file.read()
        markdown_file.close()
        text = markdown_to_blocks(markdown)
        expected_text = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]
        self.assertEqual(text, expected_text)

    def test_block_to_blocktype_eq(self):
        markdown_file = open(
            r"/home/szymon/Programowanie/StaticStieGenerator/content/test.md"
        )
        markdown = markdown_file.read()
        markdown_file.close()
        markdown_block_list = markdown_to_blocks(markdown)
        block = block_to_blocktype(markdown_block_list[0])
        block2 = block_to_blocktype(markdown_block_list[1])
        block3 = block_to_blocktype(markdown_block_list[2])
        expected_types = [
            BlockType.Heading,
            BlockType.Paragraph,
            BlockType.UnorderedList,
        ]
        self.assertEqual(block, expected_types[0])
        self.assertEqual(block2, expected_types[1])
        self.assertEqual(block3, expected_types[2])

    def test_paragraph(self):
        self.maxDiff = None
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # self.assertEqual(
        #    html,
        #    "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        # )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
