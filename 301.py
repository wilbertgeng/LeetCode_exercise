"""301. Remove Invalid Parentheses"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ## Practice:
        def isValid(s):
            cnt = 0
            for n in s:
                if n == "(":
                    cnt += 1
                elif n == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}
        newLevel = set()

        while True:
            valid = filter(isValid, level)
            if valid:
                return valid
            for s in level:
                for i in range(len(s)):
                    newLevel.add(s[:i]+s[i+1:])
            level = newLevel
            newLevel = set() ## !!







        #####
        def isValid(s):
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s} # use set here
        while True:
            valid = filter(isValid, level)
            if valid:
                return valid
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}















#####
