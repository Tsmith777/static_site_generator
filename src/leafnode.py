from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, text, props=None):
        super().__init__(tag, text, None, props)
    
    def to_html(self):
        if self.text is None:
            raise ValueError("no text")
        if self.tag is None:
            return self.text
        return f"<{self.tag}{super().props_to_html()}>{self.text}</{self.tag}>"