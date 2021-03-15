"""993. Cousins in Binary Tree"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        queue = [root]
        d ={root.val:root.val} # !! root's parent is itself
        tmp = []
        while queue:
            node = queue.pop(0)
            if node.left:
                tmp.append(node.left)
                d[node.left.val] = node.val
            if node.right:
                tmp.append(node.right)
                d[node.right.val] = node.val
            if not queue:
                if x in d and y in d and d[x] != d[y]:
                    return True
                queue = tmp
                tmp = []
                d = {}
        return False















#####
