"""572. Subtree of Another Tree (easy)"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        ########## Practice:
        def convert(node):
            if node:
                return "#" + str(node.val) + "!" + convert(node.left) + convert(node.right)
            else:
                return "$"

        return convert(t) in convert(s)




    ### convert tree to string: beat 100%
        def convert(p):
            return "#" + str(p.val) + "!" + convert(p.left) + convert(p.right) if p else "$"

        return convert(t) in convert(s)

 #####  DFS

    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and self.isMatch(s.left, t.left) and
        self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
