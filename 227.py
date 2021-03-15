"""227. Basic Calculator II"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        return self.helper(l)

    def helper(self, s):
        stack = []
        sign = "+"
        num = 0
        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = 10*num + int(c)
            if c == "(": ## be careful don't use multiple consecutive elif
                num = self.helper(s)
            if (not c.isdigit() and c != " ") or len(s) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0

            if c == ")":
                break
        return sum(stack)
