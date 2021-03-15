"""131. Palindrome Partitioning"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ## Practice :
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(path)
            return
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                self.dfs(s[i+1:], path + [s[:i+1]])

        ###### Practice:

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path+[s[:i]], res)
        res = []
        dfs(s, [], res)
        return res

        ## R2:
        res = []
        if not s:
            return res

        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path + [s[:i]], res)

            return

        dfs(s, [], res)
        return res



        ## R1:
        res = []
        if not s:
            return res

        def dfs(s, path, res):
            if  not s:
                res.append(path)
        # be careful of this this range
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path + [s[:i]], res)

        dfs(s, [], res)

        return res
