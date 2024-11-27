import fsutils
from generator import generate_page, generate_page_recursive


def main():
    fsutils.clean_dir("/home/szymon/Programowanie/StaticStieGenerator/public/")
    fsutils.copy_tree(
        "/home/szymon/Programowanie/StaticStieGenerator/static/",
        "/home/szymon/Programowanie/StaticStieGenerator/public/",
    )
    generate_page_recursive(
        "/home/szymon/Programowanie/StaticStieGenerator/content/",
        "/home/szymon/Programowanie/StaticStieGenerator/content/",
        "/home/szymon/Programowanie/StaticStieGenerator/template.html",
        "/home/szymon/Programowanie/StaticStieGenerator/public/",
    )


if __name__ == "__main__":
    main()
