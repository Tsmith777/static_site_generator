class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("Both tag and value are None")
            return self.value
        
        # Self-closing tags
        if self.tag in ["img", "hr", "br"] and not self.children:
            return f"<{self.tag}{self.props_to_html()}>"
        
        # Node with value (text content)
        if self.value is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        # Node with children
        if self.children is not None:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
        # Empty node
        return f"<{self.tag}{self.props_to_html()}></{self.tag}>"

    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.text}, children: {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.text == other.text
            and self.props == other.props
            and self.children == other.children
        )