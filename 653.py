"""653. Two Sum IV - Input is a BST"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []
        self.dfs(root, nums)
        d = {}

        n = len(nums)
        for i in range(n):
            if (k - nums[i]) not in d:
                d[nums[i]] = i

            else:
                return True

        return False


    def dfs(self, node, nums):
        if not node:
            return

        self.dfs(node.left, nums)
        nums.append(node.val)
        self.dfs(node.right, nums)
######
if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False
