from enum import Enum
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        
        parts = node.text.split(delimiter)

        if len(parts) % 2 != 1:
            new_list.append(node)
            continue
        
        for index, part in enumerate(parts):
            if index % 2 == 0:
                new_list.append(TextNode(part, TextType.TEXT))
            else:
                new_list.append(TextNode(part.strip(), text_type))

    return new_list