"""652. Find Duplicate Subtrees"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        hashmap = {}
        res = []
        self.solve(root, hashmap)
# Concept - We can use a hashmap to store the all the trees and their roots
        for val, node in hashmap.values():
            if val > 1:
                res.append(node) ## append node
        return res


    def solve(self, node, hashmap):
        if not node:
            return "X"

        a = self.solve(node.left, hashmap)
        b = self.solve(node.right, hashmap)
 # Pre-order tree representation for storing the tree
        temp = str(node.val) + " " + a + " " + b

        if temp not in hashmap:
            hashmap[temp] = [1, node]
        else:
            hashmap[temp][0] += 1

        return temp
