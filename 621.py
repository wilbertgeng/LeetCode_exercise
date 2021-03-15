"""621. Task Scheduler"""

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = collections.Counter(tasks).value()
        M = Max(task_count)
        mct = task_count.count(M)
        return max(len(tasks), (M-1)*(n+1)+mct)
