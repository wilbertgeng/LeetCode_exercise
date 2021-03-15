"""705. Design HashSet"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SIZE = 10000
        self.buckets = [[] for _ in range(self.SIZE)]

    def _index(self, key):
        bucket = self.buckets[key%self.SIZE]
        for i, num in enumerate(bucket):
            if num == key:
                return i, bucket
        return -1, bucket

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx, bucket = self._index(key)
        if idx == -1:
            bucket.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx, bucket = self._index(key)
        if idx >= 0:
            bucket.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        idx, bucket = self._index(key)
        if idx >= 0:
            return True
        else:
            return False













        ##########
