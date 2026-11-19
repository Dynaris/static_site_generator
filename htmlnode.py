class HTMLNode():

    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""

        if self.props == None:
            return ""
        else:
            for attribute, value in self.props.items():
                props_string += (f' {attribute}="{value}"')

        return props_string

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props = props)

    def to_html(self):

        if self.value == None:
            raise ValueError("Leaf node has no value.")

        if self.tag == None:
            return self.value
        
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props = props)

    def to_html(self):
        result = ""

        if self.tag == None:
            raise ValueError("No Tag value was selected.")

        if self.children == None:
            raise ValueError("No HTMLNode children were selected.")

        else:
            for child in self.children:
                while child != None:
                    child_result = self.to_html(child)
                    result += child_result

        return result