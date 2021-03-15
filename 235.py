"""235. Lowest Common Ancestor of a Binary Search Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ###### Practice:
        s = min(p.val, q.val)
        l = max(p.val, q.val)
        return self.dfs(root, s, l)

    def dfs(self, node, s, l):
        if not node:
            return None
        if node.val > l:
            return self.dfs(node.left,s, l)
        if node.val < s:
            return self.dfs(node.right, s ,l)
        if s <= node.val <= l:
            return node
        
        ### DFS recursive:
        if not root or not p or not q:
            return None
        if (root.val < min(p.val, q.val)):

            ### !! return self.DFS not just simply execute
            return self.lowestCommonAncestor(root.right, p, q)
        elif (root.val > max(p.val, q.val)):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root



        ### Iterative:
        while root:
            if p.val < root.val > q.val and root.left:
                root = root.left
            elif p.val > root.val < q.val and root.right:
                root = root.right
            else:
                return root ## returntype: TreeNode
