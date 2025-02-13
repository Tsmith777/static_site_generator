def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_list = [block.strip() for block in blocks if block.strip()]
    return block_list