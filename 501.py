"""501. Find Mode in Binary Search Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nums = []
        if not root:
            return None

        self.dfs(root, nums)
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        res = []
        mode = max(d.values())
        for key in d:
            if d[key] == mode:
                res.append(key)
        return res



    def dfs(self, node, nums):
        if not node:
            return

        self.dfs(node.left, nums)
        nums.append(node.val)
        self.dfs(node.right, nums)
