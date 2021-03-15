"""667. Beautiful Arrangement II"""

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = range(1, n-k)
        for d in range(k+1):
            if d%2 == 0:
                ans.append(n - k + d/2)
            else:
                ans.append(n - d/2)
        return ans


        
