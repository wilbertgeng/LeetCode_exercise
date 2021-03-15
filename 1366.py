"""1366. Rank Teams by Votes"""

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        count = {}
        for l in votes[0]:
            count[l] = [0]*len(votes[0])+ [l]

        for v in votes:
            for idx, l in enumerate(v):
                count[l][idx] -= 1
        res = sorted(votes[0], key = count.get)
        res = ''.join(res)
        return res
        ########
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        print(count)
        print(count.get)
        print(sorted(votes[0], key=count.get))
        return ''.join(sorted(votes[0], key=count.get))

s = Solution()
ans = s.rankTeams(["ABC","ACB","ABC","ACB","ACB"])
print(ans)
