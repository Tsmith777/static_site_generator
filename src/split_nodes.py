from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue

        current_text = node.text
        for image_text, image_url in images:
            sections = current_text.split(f"![{image_text}]({image_url})", 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(image_text, TextType.IMAGE, image_url))
            current_text = sections[1]
        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue

        current_text = node.text
        for link_text, link_url in links:
            sections = current_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, link_url))
            current_text = sections[1]
        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    return result