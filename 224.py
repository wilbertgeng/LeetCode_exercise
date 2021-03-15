"""224. Basic Calculator"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find int in the str
        l = list(s) # l is a list of strings
        return self.helper(l)

    def helper(self, s):
        stack = []
        num = 0
        sign = "+"
        while len(s) > 0:
            c = s.pop(0) # pop 1st element !!
            if c.isdigit():
            #The isdigit() method returns True
            #if all characters in a string are digits.
            #If not, it returns False.
                num = num*10 + int(c)
            if c == "(":
                num = self.helper(s)

          #  if c.isdigit() and len(s) == 0:
            #    stack.append(num)
            if (not c.isdigit() and c != " ") or len(s) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)

                num = 0
                sign = c
            if c == ")":
                break
        return sum(stack)
