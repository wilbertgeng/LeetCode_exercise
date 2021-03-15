"""111. Minimum Depth of Binary Tree"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ##### Practice:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        ###### DFS:
        if root is None:
            return 0

        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        ###### BFS:
        if not root:
            return 0
        queue = collections.deque([(root, 1)]) # root 本身就是一层，depth 初始化为 1
        while queue:
            node, level = queue.popleft() #将当前队列中的所有节点向四周扩散
            if node:
                if not node.left and not node.right:
                    return level
                else: # 将 cur 的相邻节点加入队列
                    queue.append((node.left, level+1)) #这里增加步数
                    queue.append((node.right, level+1))
