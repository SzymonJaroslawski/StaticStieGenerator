from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        new_children = list()

        if self.tag is None or self.tag == "":
            raise Exception("ValueError: Expected tag")

        if self.children is None or not self.children:
            raise Exception("ValueError: Expected children")

        for child in self.children:
            if isinstance(child, ParentNode):
                new_children.append(child.to_html())

            if isinstance(child, LeafNode):
                new_children.append(child.to_html())

        return f"<{self.tag}{self.props_to_html()}>{"".join(new_children)}</{self.tag}>"
