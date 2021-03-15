"""17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ### Practice:
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []
        tmp = []
        for i in digits:

            for j in map[i]:
                if res:
                    for k in res:
                        tmp.append(k+j)
                else:
                    tmp.append(j)
            res = tmp
            tmp = []
        return res
        ## Practice:
        if not digits:
            return []
        if len(digits) == 1:
            return [i for i in map[digits]]
        prev = self.letterCombinations(digits[:-1])
        curr = [i for i in map[digits[-1]]]
        res = []
        for n in prev:
            for m in curr:
                res.append(n+m)

        return res


        ## Recursion: Practice:
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in map[digits[0]]]
        prev = self.letterCombinations(digits[:-1])
        curr = [i for i in map[digits[-1]]]
        res = []
        for i in prev:
            for j in curr:
                res.append(i+j)
        return res

        # Practice:
        d = {'2':"abc", '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        tmp = []
        for i in digits:
            for l in d[i]:
                if not res:
                    tmp.append(l)
                else:
                    for n in res:
                        tmp.append(n+l)
            res = tmp
            tmp = []
        return res









        ## R2:
        result = []
        if digits == "":
            return result
        else:
            result = [""]
        keys = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno"
        , "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ## sythax 2:
        for d in digits:
            temp = result
            result = []
            for a in keys[d]:
                for l in temp:
                    l= l+a
                    result += [l]
       ## sythax simplified
        for d in digits:
            result = [l + a for l in result for a in keys[d]]
        ## result
        return result







        ## R1:
        all_cbn = [""] if digits else []
        digit_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno"
        , "7":"pqrs", "8":"tuv", "9":"wxyz"}
        for d in digits:
            all_cbn = [p + q for p in all_cbn for q in digit_dict[d]]

        return all_cbn
