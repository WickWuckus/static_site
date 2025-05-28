import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node3 = TextNode("Sample url", TextType.NORMAL_TEXT, "www.work.biz")
        node4 = TextNode("Sample image", TextType.IMAGE, "www.img.co")
        self.assertNotEqual(node3, node4)
    def test_assert_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)
    def test_assert_is_not_none(self):
        node3 = TextNode("Sample url", TextType.NORMAL_TEXT, "www.work.biz")
        node4 = TextNode("Sample image", TextType.IMAGE, "www.img.co")
        self.assertIsNotNone(node3.url)
        self.assertIsNotNone(node4.url)
    def test_assert_is_not(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node3 = TextNode("Sample url", TextType.NORMAL_TEXT, "www.work.biz")
        self.assertIsNot(node, node3)
    def test_assert_is(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertIs(node, node)
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertEqual(node.text, node2.text)
    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node.text_type, node2.text_type)
    
                


if __name__ == "__main__":
    unittest.main()