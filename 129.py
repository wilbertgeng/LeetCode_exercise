"""129. Sum Root to Leaf Numbers"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = []
        self.dfs(root, '')
        nums = []
        for num in self.res:
            nums.append(int(num))
        return sum(nums)

    def dfs(self, node, path):
        path += str(node.val)
        if not node.left and not node.right:
            self.res.append(path)
            return
        if node.left:
            self.dfs(node.left, path)
        if node.right:
            self.dfs(node.right, path)













########
