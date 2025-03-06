from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_children import text_to_children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode(tag="div", children=[])

    for block in blocks:
        type = block_to_block_type(block)

        if type == "paragraph":
            child = ParentNode(tag="p", children=text_to_children(block))

        elif type == "heading":
            heading_level = is_heading(block)
            heading_text = extract_heading_text(block)
            child = ParentNode(tag=f"h{heading_level}", children=text_to_children(heading_text))

        elif type == "code":
            lines = block.split("\n")

            if lines[0].strip() == "```" and lines[-1].strip() == "```":
                code_content = "\n".join(block.split("\n")[1:-1])
            else:
                code_content = block
            child = ParentNode(tag="pre", children=[])
            code_node = ParentNode(tag="code", children=text_to_children(code_content))
            child.children.append(code_node)

        elif type == "quote":
            lines = block.split("\n")
            cleaned_lines = [line[1:].strip() if line.startswith(">") else line.strip() for line in lines]

            quote_content = " ".join(cleaned_lines)
            child = ParentNode(tag="blockquote", children=text_to_children(quote_content))

        elif type == "unordered_list":
            child = ParentNode(tag="ul", children=[])
            lines = block.split("\n")

            for line in lines:
                if line and (line.startswith("*") or line.startswith("-")):
                    stripped_line = line[1:].strip()

                    if not stripped_line:
                        print(f"Skipping empty list item in block: {block}")
                        continue

                    list_item = ParentNode(tag="li", children=text_to_children(stripped_line))
                    child.children.append(list_item)

        elif type == "ordered_list":
            child = ParentNode(tag="ol", children=[])

            lines = block.split("\n")

            for line in lines:
                if line:  # Ensure line is non-empty
                    parts = line.split(".", 1)  # Split by "."
                    if len(parts) == 2 and parts[0].strip().isdigit():  # Check numbering
                        stripped_line = parts[1].strip()  # Extract list item text

                        if not stripped_line:
                            print(f"Skipping empty list item in block: {block}")
                            continue

                        list_item = ParentNode(tag="li", children=text_to_children(stripped_line))
                        child.children.append(list_item)

        else:
            print(f"ERROR: Unrecognized block type '{type}' for block: {block}")
            continue

        parent.children.append(child)

    return parent

def is_heading(block):
    if not block.startswith("#"):
        return None
    
    parts = block.split(" ", 1)
    if len(parts) < 2:
        return None
        
    heading_level = len(parts[0])
    if heading_level < 1 or heading_level > 6:
        return None
        
    if not parts[1].strip():
        return None
        
    return heading_level

def extract_heading_text(block):
    parts = block.split(" ", 1)
    return parts[1].strip()