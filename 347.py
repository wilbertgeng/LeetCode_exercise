"""347. Top K Frequent Elements"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ### R2:
        hs = {}
        frq = {}
        for num in nums:
            if num not in hs:
                hs[num] = 1
            else:
                hs[num] += 1

        for n, v in hs.iteritems():
            if v not in frq:
                frq[v] = [n] ## list needs append later
            else:
                frq[v].append(n)

        rank = []

        for x in range(len(nums), 0, -1):
            if x in frq:
                for a in frq[x]:
                    rank.append(a)

        return rank[:k]


        ### R1:
        hs = {}
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z, v in hs.iteritems():
            if v not in freq:
                freq[v] = [z]
            else:
                freq[v].append(z)

        rank = []

        for x in range(len(nums), 0, -1):
            if x in freq:
                for a in freq[x]:
                    rank.append(a)

        return [rank[i] for i in range(0, k)]
