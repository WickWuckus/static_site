from textnode import *
from htmlnode import *

def main():
	sample_text = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(sample_text)
	sample_html = HTMLNode(
            "a", 
            "Test Link", 
            None, 
            {"href": "https://www.google.com", "target": "_blank",}
            )
	print(sample_html)

main()
