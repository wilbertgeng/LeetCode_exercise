"""767. Reorganize String"""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        s = Counter(S)
        pq = []
        for key, value in s.items():
            pq.append((-value, key))
        heapq.heapify(pq)
        v_prev = 0
        k_prev = ""
        while pq: # two smallest heaps alternate
            v, k = heapq.heappop(pq)
            res += [k]
            if v_prev < 0:
                heapq.heappush(pq, (v_prev, k_prev))
            v += 1
            v_prev, k_prev = v, k

        res = "".join(res)
        return res if len(res) == len(S) else ""
