"""93. Restore IP Addresses"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ## Practice:
        """ DFS Backtrack string, iterate through first 3 eles for each
        string. """
         self.res = []
        self.dfs(0, "", s)
        return self.res

    def dfs(self, cnt, path, s):
        if cnt > 4:  ## !! don't forget
            return
        if cnt == 4 and not s:
            self.res.append(path[:-1])
            return
        for i in range(1, len(s)+1):
            if s[:i] == "0" or (s[0] != '0' and 0< int(s[:i]) < 256):
                self.dfs(cnt + 1, path + s[:i] + '.', s[i:])
        



        ##
        res = []
        self.backtrack(s, 0, "", res)
        return res

    def backtrack(self, s, idx, path, res):
        if idx > 4:
            return
        if idx == 4 and not s:
            res.append(path[:-1])
            return # don't forget to end this track
        for i in range(1, len(s)+1):
            # each integer is between 0 and 255
            # cannot have leading zeros
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i])< 256):
                self.backtrack(s[i:], idx+1, path+s[:i]+".", res)
