"""298. Binary Tree Longest Consecutive Sequence"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1
        if not root:
            return 0
        if root.left:
            self.dfs(root, root.left, 1)
        if root.right:
            self.dfs(root, root.right, 1)
        return self.res

    def dfs(self, prev, curr, cnt):
        if not curr:
            self.res = max(self.res, cnt)
            return
        if curr.val == prev.val+1:
            cnt += 1
            prev = curr
            self.dfs(prev, curr.left, cnt)
            self.dfs(prev, curr.right, cnt)
        else:
            self.res = max(self.res, cnt)
            prev = curr
            self.dfs(prev, curr.left, 1)
            self.dfs(prev, curr.right, 1)
