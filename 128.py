"""128. Longest Consecutive Sequence"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##### Practice
        d = {}
        nums.sort()
        if not nums:
            return 0
        for n in nums:
            if n - 1 in d:
                d[n] = d[n-1] + 1
            else:
                d[n] = 1
        return max(d.values())

        
        ## R1: use set
        st = set(nums)

        length = 0
        for num in nums:
            if num -1 not in st:
                tmp = 1
                while num+1 in st:
                    tmp += 1
                    num += 1
                length = max(length, tmp)

        return length



        ## wrong answer
        d = {}
        nums.sort()

        for num in nums:
            if num not in d:
                d[num] = 1

        res = 0
        for num in nums:
            if num-1 in d:
                d[num] += d[num-1]

            res = max(res, d[num])

        return res
