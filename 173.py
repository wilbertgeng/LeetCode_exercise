"""173. Binary Search Tree Iterator"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushall(root)

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushall(node.right)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def pushall(self, node):
        while node:
            self.stack.append(node)
            node = node.left












########
