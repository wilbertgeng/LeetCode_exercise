"""337. House Robber III"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Practice:
        if not root:
            return 0
        prev, now = self.dfs(root)
        return now

    def dfs(self, node):
        if not node:
            return (0, 0)
        prev1, now1 = self.dfs(node.left)
        prev2, now2 = self.dfs(node.right)
        prev = prev1 + prev2
        now = now1 + now2
        return (now, max(prev+node.val, now))



        ### R3:
        def superrob(node):
            if not node:
                return (0, 0)
            left = superrob(node.left)
            right = superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)

            return (now, later)

        return max(superrob(root))

        ###### R2:
        # returns tuple of size two (now, later)
        # now: max money earned if input node is robbed
        # later: max money earned if input node is not robbed
        def superrob(node):
            if not node:
                return (0, 0)

            left, right = superrob(node.left), superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(right) + max(left)

            return (now, later)

        return max(superrob(root))


        ####### R1:
        def superrob(node):
            if not node: return (0, 0)

            left, right = superrob(node.left), superrob(node.right)

            now = node.val + left[1] + right[1]
            later = max(right) + max(left)

            return (now, later)


        return max(superrob(root))
