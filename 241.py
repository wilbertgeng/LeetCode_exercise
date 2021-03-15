"""241. Different Ways to Add Parentheses"""

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ## Practice:
        def compute(input):
            res = []
            if "*" not in input and '+' not in input and "-" not in input:
                res.append(int(input))
            for i, n in enumerate(input):
                if n in "+-*":
                    left = compute(input[:i])
                    right = compute(input[i+1:])
                    for v1 in left:
                        for v2 in right:
                            res.append(eval(str(v1)+n+str(v2)))
            return res

        return compute(input)



        ### Review practice:
        res = []
        if "+" not in input and "-" not in input and "*" not in input:
            res.append(int(input))

        for n, v in enumerate(input):
            if v == "+" or v == "-" or v == "*":
                first = self.diffWaysToCompute(input[:n])
                second = self.diffWaysToCompute(input[n+1:])
                for i, v1 in enumerate(first):
                    for j, v2 in enumerate(second):
                        if v == "+":
                            res.append(v1 + v2)
                        elif v == "-":
                            res.append(v1 - v2)
                        elif v == "*":
                            res.append(v1 * v2)

        return res
################












        res = []

        if "+" not in input and "-" not in input and "*" not in input:
            res.append(int(input))

        ## recursive
        for n, v in enumerate(input):
            if v == "+" or v== "-" or v == "*":
                firstlist = self.diffWaysToCompute(input[:n])
                secondlist = self.diffWaysToCompute(input[n+1:])
                for i, v1 in enumerate(firstlist):
                    for j, v2 in enumerate(secondlist):
                        if v == "+":
                            res.append(v1 + v2)
                        elif v == "-":
                            res.append(v1 - v2)
                        elif v == "*":
                            res.append(v1 * v2)

        return res
