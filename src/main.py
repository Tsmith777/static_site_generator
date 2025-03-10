import os
import sys
import shutil
from textnode import TextNode, TextType
from generate_pages_recursive import generate_pages_recursive

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
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static("static","docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()