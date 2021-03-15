"""752. Open the Lock"""

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = collections.deque()
        dead_end = set(deadends) #记录需要跳过的死亡密码
        visited = set("0000")
        queue.append(("0000", 0)) #从起点开始启动广度优先搜索

        while queue:
            string, step = queue.popleft()
            if string in dead_end:
                continue
            if string == target: # 判断是否到达终点
                return step
            # 将当前队列中的所有节点向周围扩散
            for i in range(4):
                for j in (-1, 1):
                    num = int(string[i])
                    new_string = string[:i] + str((num+j)%10) + string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, step+1)) #在这里增加步数
        return -1 #如果穷举完都没找到目标密码，那就是找不到了
