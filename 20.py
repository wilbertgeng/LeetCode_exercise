
##Valid parenthesis
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## R2:
        map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:

            if char in map:
                if not stack:
                    return False
                else:
                    top_ele = stack.pop()
                    if top_ele != map[char]:
                        return False

            else:
                stack.append(char)

        return not stack

    
        ## R1:
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
