"""394. Decode String"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ### Practice:
        curstring = ''
        curnum = 0
        stack = []
        for i in s:
            if i == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif i.isdigit():
                curnum = 10*curnum + int(i)
            elif i == ']':
                prevnum = stack.pop()
                prevstring = stack.pop()
                curstring = prevstring + prevnum*curstring
            else:
                curstring += i

        return curstring




        ##### Practice:
        curnum = 0
        curstring = ''
        stack = []
        for i in s:
            if i == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif i.isdigit():
                curnum = curnum*10 + int(i)
            elif i == ']':
                prevnum = stack.pop()
                prevstring = stack.pop()
                curstring = prevstring + prevnum*curstring
            else:
                curstring += i

        return curstring


        ############
        curstring = ""
        curnum = 0
        stack = []

        for i in s:
            if i == "[":
                stack.append(curstring)
                stack.append(curnum)
                curstring = ""
                curnum = 0

            elif i.isdigit():
                curnum = curnum*10 + int(i)

            elif i == "]":
                num = stack.pop() # num is not curnum
                prevstring = stack.pop()
                curstring = prevstring + num*curstring

            else:
                curstring += i

        return curstring
