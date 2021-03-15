"""230. Kth Smallest Element in a BST"""

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ### practice
        self.res = []
        self.dfs(root)
        return self.res[k-1]

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)

        ######## R2:
        res = []
        self.dfs(root, res)
        return res[k-1]

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)


        ######## R1:
        count = []
        self.helper(root, count)
        return count[k - 1]

    def helper(self, root, count):

        if not root:
            return
        self.helper(root.left, count)
        count.append(root.val)
        self.helper(root.right, count)
