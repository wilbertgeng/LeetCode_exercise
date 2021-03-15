"""437. Path Sum III"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ######## Practice
        self.res = 0
        oldpaths = {0:1}
        self.dfs(root, sum, 0, oldpaths)
        return self.res
    def dfs(self, node, target, currpath, oldpaths):
        if not node:
            return
        currpath += node.val
        oldpath = currpath - target
        self.res += oldpaths.get(oldpath, 0)
        oldpaths[currpath] = oldpaths.get(currpath, 0) + 1
        self.dfs(node.left, target, currpath, oldpaths)
        self.dfs(node.right, target, currpath, oldpaths)
        oldpaths[currpath] -= 1



        """ R2:  A fast way beat 98%: dfs post-order. Use cache (dict)"""
        self.res = 0
        cache = {0:1}
        self.dfs(root, sum, 0, cache) #cache gets updated every recursion,
        ### self.res automatically updated
        return self.res

    def dfs(self, node, target, currentpathSum, cache):
        # exit condition
        if not node:
            return
        # calculate currPathSum and required oldPathSum
        currentpathSum += node.val
        oldpathSum = currentpathSum - target
        # update result and cache:
        self.res += cache.get(oldpathSum, 0)
        cache[currentpathSum] = cache.get(currentpathSum, 0) + 1
         # dfs breakdown
        self.dfs(node.left, target, currentpathSum, cache)
        self.dfs(node.right, target, currentpathSum, cache)
        # when move to a different branch, currentpathSum is no longer available hence -1
        cache[currentpathSum] -= 1

    """  R2: too slow"""
        self.pathSum = 0
        dfs(root, sum)
        return self.pathSum

    def dfs(self, node, target):
        if node is None:
            return

        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.pathSum += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)


######### R1:
        self.res = 0
        cache = {0:1}
        self.dfs(root, sum, 0, cache)

        return self.res

    def dfs(self, node, target, currentpath, cache):
        if node is None:
            return

        currentpath += node.val
        oldpath = currentpath - target
        self.res += cache.get(oldpath, 0)
        cache[currentpath] = cache.get(currentpath, 0) + 1

        self.dfs(node.left, target, currentpath, cache)
        self.dfs(node.right, target, currentpath, cache)
#### cache vale needs to be updated back to previous level
        cache[currentpath] -= 1
