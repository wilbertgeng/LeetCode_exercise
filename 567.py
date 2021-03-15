"""567. Permutation in String
Medium"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        window = {}
        left = 0
        right = 0
        valid = 0
        length = float('inf')
        while right < len(s):
            d = s[right] # d 是将移入窗口的字符
            right += 1
            if d in need: #进行窗口内数据的一系列更新
                window[d] = window.get(d, 0) + 1
                if window[d] == need[d]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left == len(t):
                # 在这里check
                if valid == len(need):
                    return True
                l = s[left]
                left += 1 # 左移窗口
                if l in need: # 进行窗口内数据的一系列更新
                    if window[l] == need[l]:
                        valid -= 1
                    window[l] -= 1

        return False
