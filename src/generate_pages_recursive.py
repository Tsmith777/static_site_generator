import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, entry).replace(".md", ".html")

            generate_page(entry_path, template_path, dest_path, basepath)

        elif os.path.isdir(entry_path):
            new_dest_dir_path = os.path.join(dest_dir_path, entry)

            os.makedirs(new_dest_dir_path, exist_ok=True)

            generate_pages_recursive(entry_path, template_path, new_dest_dir_path, basepath)