"""134. Gas Station"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ##
        if not gas or not cost or sum(gas) < sum(cost):
            return -1

        



        ##
