"""297. Serialize and Deserialize Binary Tree (Hard)"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.dfs(root)
        return ' '.join(self.res)

    def dfs(self, node):
        if not node:
            self.res.append('*')
            return
        self.res.append(str(node.val))
        self.dfs(node.left)
        self.dfs(node.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data_vals = iter(data.split())
        return self.decode()
    def decode(self):
        node_val = next(self.data_vals)
        if node_val == '*':
            return None
        node = TreeNode(node_val)
        node.left = self.decode()
        node.right = self.decode()
        return node




class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.nodes_inorder = []
        self.dfs(root)
        res = ' '.join(self.nodes_inorder) ## convert list to string with seperator ' '
        return res

    def dfs(self, root):
        if not root:
            self.nodes_inorder.append('#')
            return
        self.nodes_inorder.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.vals = iter(data.split()) ### split() convert string to list's iterator
        return self.decode()

    def decode(self):
        val = next(self.vals)
        if val == "#":
            node = None
        else:
            node = TreeNode(int(val))
            node.left = self.decode()
            node.right = self.decode()
        return node




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
