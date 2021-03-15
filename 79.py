"""79. Word Search"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # R2:
        if not word:
            return True
        if not board:
            return False

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, i, j):
                    return True
        return False

    def backtrack(self, board, word, i, j):
        m = len(board)
        n = len(board[0])
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = ' '
            if i < m-1 and self.backtrack(board, word[1:], i+1, j):
                return True
            if i > 0 and self.backtrack(board, word[1:], i-1, j):
                return True
            if j < n-1 and self.backtrack(board, word[1:], i, j+1):
                return True
            if j > 0 and self.backtrack(board, word[1:], i, j-1):
                return True

            board[i][j] = word[0]
            return False
        else:
            return False




        ##### R1:
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs_exist_helper(board, word, i, j):
                    return True
        return False
    def dfs_exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            # exit condition
            if not word[1:]:
                return True
            board[i][j] = " " #indicate used cell, in case cell check goes backwards
            # this checked cell will be restored by the end of this loop
            if i > 0 and self.dfs_exist_helper(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.dfs_exist_helper(board, word[1:],i+1, j):
                return True
            if j > 0 and self.dfs_exist_helper(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.dfs_exist_helper(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] #update the cell to its original value
            return False
        else:
            return False
