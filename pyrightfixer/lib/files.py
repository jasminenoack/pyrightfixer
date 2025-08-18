import os


def get_file_list(path: str) -> list[str]:
    files = []
    path = os.path.abspath(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' does not exist.")
    if not os.path.isdir(path) and path.endswith(".py"):
        files.append(path)
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            files.extend(get_file_list(os.path.join(root, filename)))
    return files
