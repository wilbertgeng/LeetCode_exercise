"""530. Minimum Absolute Difference in BST"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        nums = []
        self.dfs(root, nums)
        res = float('inf')
        for i in range(len(nums)-1):
            res = min(res, abs(nums[i]-nums[i+1]))

        return res

    def dfs(self, node, nums):
        if not node:
            return None

        self.dfs(node.left, nums)
        nums.append(node.val)
        self.dfs(node.right, nums)



########## same time, even larger, looks shorter though
 def getMinimumDifference(self, root):
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(b - a for a, b in zip(L, L[1:]))
