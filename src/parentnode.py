from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("missing children value")
        full_string = ""
        for child in self.children:
            full_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{full_string}<\/{self.tag}>"