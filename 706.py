"""706. Design HashMap"""

## Practice
class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.SIZE = 1000
        self.hashing = [ListNode(-1)]*self.SIZE

    def put(self, key, value):
        head = self.hashing[key%self.SIZE]
        current = head.next
        while current:
            if current.key == key:
                break
            current = current.next
        else:
            current = ListNode(key)   # be careful! Need to build a listnode here
            current.next = head.next
            head.next = current
        current.val = value

    def get(self, key):
        head = self.hashing[key%self.SIZE]
        current = head
        while current:
            if current.key == key:
                break
            current = current.next
        else:
            return -1
        return current.val

    def remove(self, key):
        head = self.hashing[key%self.SIZE]
        current = head
        while current and current.next:
            if current.next.key == key:
                break
            current = current.next
        else:
            return None
        current.next = current.next.next



class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None
class MyHashMap(object):
# use linkedList to realize hashmap
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SIZE = 1000
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        head = self.hashing[key%self.SIZE]
        current = head.next
        while current:
            if current.key == key:
                break # key exists, update value
            current = current.next # to avoid collision
        else:  # create a new ele in hashtable
            current = ListNode(key)
            current.next = head.next
            head.next = current
        current.val = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        current = self.hashing[key%self.SIZE].next
        while current:
            if current.key == key:
                break
            current = current.next # to avoid collision
        else:
            return -1
        return current.val

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        current = self.hashing[key%self.SIZE]
        while current and current.next:
            if current.next.key == key:
                break
            current = current.next
        else:
            return None

        current.next = current.next.next












#
