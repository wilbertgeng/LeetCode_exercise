"""232. Implement Queue using Stacks"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack, self.outstack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.outstack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        ## question: why not -->   return self.instack[0]
        self.move()
        return self.outstack[-1]
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.instack) and (not self.outstack)

    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
