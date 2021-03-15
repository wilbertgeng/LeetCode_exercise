"""76. Minimum Window Substring"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ############## sliding window Pointers
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
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    length = right - left
                    start = left
                l = s[left]
                left += 1 # 左移窗口
                if l in need: # 进行窗口内数据的一系列更新
                    if window[l] == need[l]:
                        valid -= 1
                    window[l] -= 1

        return "" if length == float('inf') else s[start:(start+length)]



        ######################
        start = 0
        n = len(s)
        target_letter_count =collections.Counter(t)
        target_len = len(t)
        min_window = ""

        for end in range(0, n):
            if target_letter_count[s[end]] > 0:
                target_len -= 1

            target_letter_count[s[end]] -= 1
             # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve

            while target_len == 0:
                window_len = end - start + 1     #test if window len is smaller than len(min_window)
                if not min_window or window_len < len(min_window):
                    min_window = s[start: end + 1] # Note the new minimum window

                target_letter_count[s[start]] += 1
                # If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_count[s[start]] > 0:
                    target_len += 1

                start += 1

        return min_window
