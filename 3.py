"""Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ############################
        window = {}
        left = 0
        right = 0
        length = float('-inf')
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1
            length = max(length, right - left)

        return 0 if length == float('-inf') else length

        
        ##############
        if s == 0:
            return 0
        map = {}
        max_length = start = 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            map[s[i]] = i

        return max_length
