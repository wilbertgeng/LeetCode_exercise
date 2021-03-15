"""617. Merge Two Binary Trees"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        ########## Practice:
        return self.dfs(t1, t2)

    def dfs(self, t1, t2):
        if not t1 and not t2:
            return None
        elif not t1 or not t2:
            return t1 or t2
        node = TreeNode(t1.val + t2.val)
        node.left = self.dfs(t1.left , t2.left)
        node.right = self.dfs(t1.right, t2.right)
        return node


        #### R2:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val) ### create a treeNode
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2




        ########### R1:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
