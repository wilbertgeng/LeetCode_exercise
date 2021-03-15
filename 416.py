"""Partition Equal Subset Sum"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## practice:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)/2
        dp = [1]+[0]*target
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
                if dp[target] != 0:
                    return True
        return False


        ## R2:
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total//2
        s = set([0])
        for n in nums:
            nums_n = []
            for i in s:
                if i + n == target:
                    return True
                if i + n < target:
                    nums_n.append(i+n)

            s.update(nums_n)

        return False

        ## My own way:
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total//2

        dp = [1]+[0]*target
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
                if dp[target] > 0:
                    return True

        return False




        ## R1:
        total = sum(nums)
        if total%2 ==1:
            return false
        target = total/2 #target Sum
        s = set([0]) # store the sum of subsets

        for n in nums:
            sum_n = []  #store sum of subsets contain n

            for i in s:
                if i + n ==target:
                    return True
                if i + n < target:
                    sums_n.append(i+n)
            s.update(sum_n)

        return False

####solution 2:
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
        return False
