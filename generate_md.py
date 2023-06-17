import os


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    return content


def write_to_markdown(file_paths, output_file="output.md"):
    with open(output_file, "w") as md_file:
        for file_path in file_paths:
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(file_path)
                md_file.write("## File: " + file_path + "\n\n")
                content = read_file(file_path)
                md_file.write(f"```{file_extension[1:]}\n")
                for line in content:
                    md_file.write(line)
                md_file.write("\n```\n")
            else:
                print("File not found: " + file_path)


if __name__ == "__main__":
    # Add the paths of your React files you'd like to include in the markdown file
    file_paths = [
        "./mokuro/__main__.py",
        "./mokuro/__init__.py",
        # "./mokuro/manga_page_ocr.py",
        # "./mokuro/overlay_generator.py",
        "./mokuro/run.py",
        # "./mokuro/script.js",
    ]
    write_to_markdown(file_paths)
