"""671. Second Minimum Node In a Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # OOP Nov 29
        self.res = float('inf')
        a = root.val
        self.find(root, a)
        return self.res if self.res != float('inf') else -1
    
    def find(self, node, a):
        if not node:
            return
        
        if a < node.val < self.res:
            self.res = node.val
        
        self.find(node.left, a)
        self.find(node.right, a)

        ### non-empty special binary tree: root.val = min(root.left.val, root.right.val)
        res = [float('inf')]
        def find2ndMin(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            find2ndMin(node.left)
            find2ndMin(node.right)

        find2ndMin(root)

        return -1 if res[0] == float('inf') else res[0]
