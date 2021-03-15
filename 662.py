"""662. Maximum Width of Binary Tree"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level = [(root, 1)]
        nxt_level = []
        width = 1 ## if only has root return 1 not 0
        while level:
            node, num = level.pop(0)
            if node.left:
                nxt_level.append((node.left, num*2))
            if node.right:
                nxt_level.append((node.right, num*2+1))
            if not level:
                if nxt_level:
                    width = max(width, nxt_level[-1][1] - nxt_level[0][1] + 1)
                level = nxt_level
                nxt_level = []

        return width



















#########
