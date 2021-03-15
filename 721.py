"""721. Accounts Merge"""

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        ### Practice:
        """1. build hash table key:email val:index
            2. use visited to mark account visited
            3. dfs use set to store emails hsare by diff accounts """
        accounts_map = collections.defaultdict(list)
        for i, act in enumerate(accounts):
            for j in range(1, len(accounts[i])):
                accounts_map[act[j]].append(i)
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                emails.add(accounts[i][j])
                for n in accounts_map[accounts[i][j]]:
                    dfs(n, emails)


        visited = [False]*len(accounts)
        res = []
        for i, act in enumerate(accounts):
            if visited[i] == False:
                name = act[0]
                emails = set()
                dfs(i, emails)
                res.append([name] + sorted(emails))
        return res





        ###
        accounts_emails_map = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                accounts_emails_map[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for n in accounts_emails_map[email]:
                    dfs(n, emails)

        res = []
        visited = [False]*len(accounts)
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res






#####
