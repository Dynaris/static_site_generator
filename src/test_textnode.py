import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is my text node", TextType.ITALIC)
        node4 = TextNode("This is my text node", TextType.CODE)
        node5 = TextNode("This is my Italic node", TextType.ITALIC)
        node6 = TextNode("This is my second Italic node", TextType.ITALIC)
        node7 = TextNode("This is the same URL", TextType.ITALIC, "www.bootdev.com")
        node8 = TextNode("This is the same URL", TextType.ITALIC, "www.bootdev.com")
        node9 = TextNode("These are different URLs", TextType.ITALIC, "www.bootdev.com")
        node10 = TextNode("These are different URLs", TextType.ITALIC, "www.ugotpwned.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
        self.assertEqual(node7, node8)
        self.assertNotEqual(node9, node10)

if __name__ == "__main__":
    unittest.main()