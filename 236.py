"""236. Lowest Common Ancestor of a Binary Tree"""

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
        ####### Practice:
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else left or right

######## R2:
        ## Recursive:
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else left or right
        ## Iterative:



######## R1:
    ### recursive:
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right
    ### Iterative: faster
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
    ### Find common parent:
        a = set()
        while p:
            a.add(p)  ## use add because it's set not list
            p = parent[p]
        while q not in a:
            q = parent[q]

        return q



# Iterative
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.left)
        ancestors = set() ## set of nodes
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]

        return q
