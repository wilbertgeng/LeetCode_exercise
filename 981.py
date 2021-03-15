"""981. Time Based Key-Value Store"""

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.dict[key]
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left)//2
            if arr[mid][1] < timestamp:
                left = mid + 1
            elif arr[mid][1] > timestamp:
                right = mid
            elif arr[mid][1] == timestamp:
                return arr[mid][0]
        return "" if right == 0 else arr[left-1][0]












#
