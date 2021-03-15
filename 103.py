"""103. Binary Tree Zigzag Level Order Traversal"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        switch = True
        level = []
        stack = [root]
        res = []
        tmp = []
        while stack:
            node = stack.pop()
            level.append(node.val)
            if switch:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not switch:
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
            if not stack:
                res.append(level)
                stack = tmp
                tmp = []
                level = []
                switch = True if not switch else False
        return res

















########
