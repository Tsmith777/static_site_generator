def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        # Check if line starts with a single # followed by a space
        if line.startswith("# "):
            # Get everything after the # and strip whitespace
            title_text = line[2:].strip()
            # Make sure there's actual text after the #
            if title_text:
                return title_text
        
    raise Exception("No h1 header found in markdown")