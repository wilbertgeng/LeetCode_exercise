"""1248. Count Number of Nice Subarrays
Medium"""

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #########
        m = [0]*50001
        res = 0
        curr = 0
        m[0] = 1
        for i in range(len(nums)):
            curr += (nums[i]%2)
            if curr >= k:
                res += m[curr-k]
            m[curr] += 1

        return res


        #######
        return self.atMost(nums, k)-self.atMost(nums, k-1)
    def atMost(self, nums, k):
        res = 0
        count = 0
        left = 0
        right = 0
        while right < len(nums):
            n = nums[right]
            count += n%2
            while count >= k:
                c = nums[left]
                count -= c%2
                left += 1
            res += right - left + 1
            right += 1
        return res
#################
        def atMost(k):
            res = 0
            left = 0
            for right in range(len(nums)):
                k -= nums[right]%2
                while k < 0:
                    k += nums[left]%2
                    left += 1
                res += right -left + 1

            return res

        return atMost(k) - atMost(k-1)










#
