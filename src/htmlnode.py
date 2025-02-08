class HTMLNode():
    def __init__(self, tag=None, text=None, children=None, props=None):
        self.tag = tag
        self.text = text
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for key in self.props:
            value = self.props[key]
            string += f" {key}=\"{value}\""
        return string

    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.text}, children: {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.text == other.text
            and self.props == other.props
            and self.children == other.children
        )