"""426. Convert Binary Search Tree to Sorted Doubly Linked List"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        ## Practice:
        if not root:
            return None
        stack = []
        head = dummy = Node(0)
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            head.right, root.left, head = root, head, root
            root = root.right
        dummy.right.left, head.right = head, dummy.right

        return dummy.right





        if not root:
            return
        prev = dummy = TreeNode(0)
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right, node.left, prev = node, prev, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right

        return dummy.right




















########
