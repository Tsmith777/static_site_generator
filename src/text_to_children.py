from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]
    