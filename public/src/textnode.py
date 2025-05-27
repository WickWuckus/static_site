from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "normal"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		if not isinstance(text_type, TextType):
			raise ValueError("text_type must be a member of TextType")

		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, text_node):
		if not isinstance(text_node, TextNode):
			return NotImplemented
		if self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url:
			return True
		else:
			return False
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
