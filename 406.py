"""406. Queue Reconstruction by Height"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ## R2:
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)

        return res

        # solution 1:
        ## 身高 h 降序、个数 k 值升序
        people = sorted(people, key = lambda x:(-x[0], x[1])) ## lambda no comma

        res = []
        for p in people:
            ## 然后将某个学生插入队列的第 k 个位置中
            res.insert(p[1], p) ## .insert(pos, element to be inserted)

        return res
