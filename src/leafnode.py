from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            if (
                self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
            ):
                return True
        return False

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise Exception("ValueError")

        if self.tag is None:
            return self.value

        props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
