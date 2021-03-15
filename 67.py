"""67. Add Binary"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #####
        res = ''
        a = list(a)
        b = list(b)
        carry = 0
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res = str(carry%2) + res
            carry = carry/2
        return res

        ####
        carry = 0
        res = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            res += str(carry%2)
            carry = carry/2

        return res[::-1]
