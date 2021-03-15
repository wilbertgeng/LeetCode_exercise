"""687. Longest Univalue Path"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## R2:
        self.longest = 0
        self.dfs(root)
        return self.longest

    def dfs(self, node):
        if not node:
            return 0
        left_len = self.dfs(node.left)
        right_len = self.dfs(node.right)
        left = left_len + 1 if node.left and node.val == node.left.val else 0
        right = right_len + 1 if node.right and node.val == node.right.val else 0

        self.longest= max(self.longest, left + right)

        return max(left, right)
            

        ## post order
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)

            return max(left, right)

        traverse(root)
        return longest[0]
