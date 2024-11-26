from os import mkdir, path
from shutil import copytree, rmtree


def clean_dir(target):
    if not path.exists(target):
        raise ValueError(f"Given path does not exist {target}")

    rmtree(target)
    mkdir(target)


def copy_tree(src, dst):
    if not path.exists(src):
        raise ValueError(f"Given path does not exist {src}")
    if not path.exists(dst):
        raise ValueError(f"Given path does not exist {dst}")

    copytree(src, dst, dirs_exist_ok=True)
