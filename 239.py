"""239. Sliding Window Maximum"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = collections.deque()

        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()

            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res










#
