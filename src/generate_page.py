import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as markdown_file, open(template_path, 'r') as template_file:
        content = markdown_file.read()
        template = template_file.read()

    try:
        title = extract_title(content)
        print(f"DEBUG: Extracted title: {title}")
    except Exception as e:
        print(f"ERROR: Failed to extract title: {str(e)}")
        return


    content_html = markdown_to_html_node(content).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as output_file:
        output_file.write(template)