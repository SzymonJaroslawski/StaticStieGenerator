import fsutils


def main():
    fsutils.clean_dir("/home/szymon/Programowanie/StaticStieGenerator/public/")
    fsutils.copy_tree(
        "/home/szymon/Programowanie/StaticStieGenerator/static/",
        "/home/szymon/Programowanie/StaticStieGenerator/public/",
    )


if __name__ == "__main__":
    main()
