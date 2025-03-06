import os
import shutil
from textnode import TextNode, TextType
from generate_page import generate_page

def copy_static(source_dir, dest_dir):
    # Delete the destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create the destination directory
    os.mkdir(dest_dir)
    
    # List all items in the source directory
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        # Check if it's a file
        if os.path.isfile(source_path):
            # Copy the file
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} to {dest_path}")
        # Check if it's a directory
        elif os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)
            print(f"Copied directory: {source_path} to {dest_path}")

def main():
    copy_static("static","public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()