def block_to_block_type(markdown_block):
    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return "code"
    elif markdown_block.startswith("#"):
        return "heading"
    elif all(line.startswith(">") for line in markdown_block.split("\n")):
        return "quote"
    elif all((line.startswith("* ") or line.startswith("- ")) for line in markdown_block.split("\n")):
        return "unordered_list"
    elif is_ordered_list(markdown_block):
        return "ordered_list"
    return "paragraph"

def is_ordered_list(markdown_block):
    lines = markdown_block.split("\n")
    expected_number = 1
    is_ordered = True

    for line in lines:
        if not line.startswith(f"{expected_number}. "):
            is_ordered = False
            break
        expected_number += 1
    return is_ordered