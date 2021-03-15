"""Validate Binary Search Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ######## Practice:
        res = []
        if not root:
            return False
        self.dfs(root, res)
        for i in range(1, len(res)):
            if res[i]<=res[i-1]:
                return False
        return True

    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)



        ##### in-order append all nodes into a list to compare
        nodes = []
        self.dfs(root, nodes)
        for i in range(len(nodes)-1):
            if nodes[i] >= nodes[i+1]:
                return False

        return True

    def dfs(self, root, nodes):
        if not root:
            return

        self.dfs(root.left, nodes)
        nodes.append(root.val)
        self.dfs(root.right, nodes)
        ######
        ##########
        # Be careful of special case: the whole left tree nodes
        # need to be smaller than root
        if not root:
            return True
        if root.val >= lessThan or root.val <= largerThan:
            return False
        return isValidBST(root.left, min(root.val, lessThan), largerThan) and
                isValidBST(root.right, lessThan, max(root.val,largerThan))
