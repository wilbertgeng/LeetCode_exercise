"""543. Diameter of Binary Tree

Given a binary tree,
you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ############ Practice
        self.res = 0
        if not root:
            return 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)

        self.res = max(self.res, l + r)
        return max(l, r) + 1




        ########### R2:
        self.ans = 0 ### OOD
        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            self.ans = max(self.ans, l + r) ### store max dismeter value for each node
            return 1 + max(l, r)
        dfs(root)
        return self.ans


        ########### R1:
        self.ans = 0

        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.ans = max(self.ans, right + left)
            return 1 + max(right, left)
        depth(root)
        return self.ans
