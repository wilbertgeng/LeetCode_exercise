"""513. Find Bottom Left Tree Value"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
        #######
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val

        ### R2:
        queue = [root]

        for node in queue:
            if node.right:
                queue.add(node.right)
            if node.left:
                queue.add(node.left)
        return node.val
