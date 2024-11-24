class HTMLNode(object):
    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            if (
                self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
            ):
                return True
        return False

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        if isinstance(self.props, dict):
            str_props = list("")
            for key, value in self.props.items():
                str_props.append(f'{key}="{value}"')
            return f" {" ".join(str_props)}"
        else:
            raise Exception("InvalidPropsType: Expected a dict")
