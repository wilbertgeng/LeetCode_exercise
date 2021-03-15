"""700. Search in a Binary Search Tree"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.righ = right

class Solution(Object):
    def searchBST(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root

        elif root.val > val:
            return self.searchBST(root.left, val)

        else:
            return self.searchBST(root.right, val)
