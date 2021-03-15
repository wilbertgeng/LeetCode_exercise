"""1423. Maximum Points You Can Obtain from Cards"""

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        points = res = sum(cardPoints[:k])
        c = cardPoints[::-1]
        for i in range(k):
            points += c[i] - cardPoints[k-i-1]
            res = max(res, points)
        return res 
