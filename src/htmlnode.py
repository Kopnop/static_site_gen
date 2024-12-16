class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        str = ""
        for key in self.props:
            str += f" {key}=\"{self.props[key]}\""
        return str

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # if not self.value:
        #     raise Exception("LeafNodes need a value")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node has no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent node has no tag")
        if not self.children:
            raise ValueError("parent node has no children")
        str = f"<{self.tag}>"
        for child in self.children:
            str += child.to_html()
        str += f"</{self.tag}>"
        return str
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"