"""Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #### Practice:
        n = len(s)
        dp = [True]+ [False]*n
        for i in range(1, n+1):
            for word in wordDict:
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
        return dp[-1]
            
        ## R2:
        dp = [False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1: i+1]:
                    if i - len(word) == -1 or dp[i-len(word)]:
                        dp[i] = True

        return dp[-1]
        #### similar
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True

        return dp[-1]


        ## R1:
        n = len(s)
        d = [False]*n

        for i in range(0, n): # recursion for backpack
            for w in wordDict: # recursion for goods
                if w == s[i - len(w) + 1: i+1] and (d[i-len(w)] or i - len(w) == -1):
                    d[i] = True

        return d[-1]
