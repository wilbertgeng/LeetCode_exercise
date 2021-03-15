"""102. Binary Tree Level Order Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            node_level = [(node.left, node.right) for node in level]
            level = [gkid for kid in node_level for gkid in kid if gkid ]

        return ans
