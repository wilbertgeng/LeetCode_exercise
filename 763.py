"""763. Partition Labels"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

### R2:  
        right_most = {letter: i for i, letter in enumerate(S)}
        right = 0
        left = 0
        res = []

        for i, letter in enumerate(S):

            right = max(right, right_most[letter])

            if i == right:
                res.append(right-left+1)

                left = right + 1

        return res


### R1:

        rightMost = {letter:i for i, letter in enumerate(S)}
        right = 0
        left = 0
        ans = []
        for i, letter in enumerate(S):

            right = max(right, rightMost[letter])

            if i == right:
                ans += [right - left + 1]

                left = i + 1

        return ans
