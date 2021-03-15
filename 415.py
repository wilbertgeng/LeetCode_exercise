"""415. Add Strings"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        res = ''

        a = list(num1)
        b = list(num2)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry%10)
            carry = carry/10

        return res[::-1]
