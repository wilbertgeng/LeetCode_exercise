"""637. Average of Levels in Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ## R2: 
        if not root:
            return []

        res = []
        current_level = [root]
        next_level = []
        while current_level:
            level_nodes = [] ## level nodes need to be update for every iteration
            for node in current_level:
                level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left) ## append node not val !!
                if node.right:
                    next_level.append(node.right)
            res.append(sum(level_nodes)/float(len(level_nodes)))

            current_level = next_level
            next_level = []
        return res





        ## R1: use list, BFS, while loop
        if root is None:
            return []

        res = []
        current_level = [root]

        while current_level:
            level_nodes = []
            next_level = []
            for node in current_level:
                level_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(sum(level_nodes)/float(len(level_nodes))) ### float
            current_level = next_level

        return res
