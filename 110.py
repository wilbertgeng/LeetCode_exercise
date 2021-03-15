"""110. Balanced Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ########## Practice

        ##############
        return self.check(root) != -1
    def check(self, node):
        if not node:
            return 0
        l = self.check(node.left)
        r = self.check(node.right)

        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1

        return 1 + max(r, l)

        #####
        def check(root):
            if not root:
                return 0

            l = check(root.left)
            r = check(root.right)

            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1

            return 1 + max(l, r)

        return check(root) != -1
