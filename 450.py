"""Delete Node in a BST"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        ### Practice
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: #found key
        # if either child is None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
        # if both childrren are not None: find the bottom right of root.left (this case)
        # or bottom left of root.right
            tmp = root.left
            min_val_right = tmp.val ## don't forget to assign this before get into loop !
            while tmp.right:
                tmp = tmp.right
                min_val_right = tmp.val
            root.val = min_val_right
            # remember to delete that bottom left/right node !
            root.left = self.deleteNode(root.left, min_val_right)

        return root


        ####
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right


            temp = root.right
            min_right_subtree = temp.val

            while temp.left:
                temp = temp.left
                min_right_subtree = temp.val

            root.val = min_right_subtree
            root.right = self.deleteNode(root.right, root.val)

        return root

##################### solution 2
class Solution(object):
    def deleteNode(self, root, key):
        if not root: return None

        if root.val == key:
            if not root.right: return root.left

            if not root.left: return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
