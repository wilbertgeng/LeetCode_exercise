"""Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ##
        if not s:
            return ""

        n = len(s)
        isPalindrome = [[False]*n for _ in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True
        for i in range(1, n):  ## !! start from 1
            isPalindrome[i][i - 1] = True

        start = 0
        lengthMax = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                isPalindrome[i][j] = isPalindrome[i + 1][j - 1] and s[i] == s[j]
                if isPalindrome[i][j] and length > lengthMax:
                    start = i
                    lengthMax = length
        return s[start: start + lengthMax]

        ### O(n^2)
        if not s:
            return s

        n = len(s)
        ans = (0, 0)
        for mid in range(n):
            ans = max(ans, self.isPalindrome(s, mid, mid))
            ans = max(ans, self.isPalindrome(s, mid, mid + 1))

        return s[ans[1]: ans[1] + ans[0]]

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return (right - left - 1, left + 1)

        # O(n^3) not pass
        if not s:
            return None

        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.is_palindrome(s, i, i + length - 1):
                    return s[i: i + length]

        return ""

    def is_palindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        return left >= right





        #### O(n^2)
        largestpalindrome = " "
        for i in range(len(s)):
            largerpalindrome_odd = self.largestpalindrome_index(s, i, i)
            largerpalindrome_even = self.largestpalindrome_index(s, i, i+1)
            if len(largerpalindrome_odd) > len(largerpalindrome_even):
                largerpalindrome = largerpalindrome_odd
            else:
                largerpalindrome = largerpalindrome_even

            largestpalindrome = largestpalindrome if len(largestpalindrome) >= len(largerpalindrome) else largerpalindrome

        return largestpalindrome

    def largestpalindrome_index(self, s, left, right):
        leftindex = rightindex = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftindex = left
                rightindex = right
            else:
                break
            left -= 1
            right += 1

        return s[leftindex:rightindex+1]
