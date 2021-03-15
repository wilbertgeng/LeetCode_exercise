"""37. Sudoku Solver"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ############ super slow but it works 
        char = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.backtrack(char, board, 0, 0)
    def backtrack(self, char, board, r, c):
        if c == 9:
            return self.backtrack(char, board, r+1, 0)
        if r == 9:
            return True

        for i in range(r, 9):
            for j in range(c, 9):
                if board[i][j] != '.':
                    return self.backtrack(char, board, i, j+1)

                for idx in range(9):
                    if not self.isValid(char[idx], board, i, j):
                        continue
                    board[i][j] = char[idx]

                    if self.backtrack(char, board, i, j+1):
                        return True
                    board[i][j] = '.'
                return False
        return False

    def isValid(self, num, board, i, j):
        for a in range(9):
            if board[i][a] == num:
                return False
            if board[a][j] == num:
                return False
            for b in range(3):
                if board[(i/3)*3 + a%3][(j/3)*3 + b] == num:
                    return False
        return True


        ############
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set),
        collections.defaultdict(set), collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r//3, c//3)].add(board[r][c])
                else:
                    visit.append((r, c))

        def dfs():
            if not visit:
                return True

            r, c = visit[0]
            t = (r//3, c//3)
            for digit in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if digit not in rows[r] and digit not in cols[c] and digit not in triples[t]:
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    triples[t].add(digit)
                    visit.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(digit)
                        cols[c].discard(digit)
                        triples[t].discard(digit)
                        visit.appendleft((r, c))
            return False
        dfs()
