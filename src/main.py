from textnode import TextNode, TextType


def main():
    test_node = TextNode("This is a text node", TextType.Bold, "https://www.boot.dev")
    print(test_node)


if __name__ == "__main__":
    main()
