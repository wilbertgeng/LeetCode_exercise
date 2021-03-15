"""773. Sliding Puzzle
Hard"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        moves = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        state = ''
        for row in board:
            for n in row:
                state+=str(n)
        start = state.index('0')
        queue = collections.deque([(state, start, 0)])
        target = "123450"
        visited = set()
        while queue:
            curr_state, idx, steps = queue.popleft()
            if curr_state == target:
                return steps
            if curr_state in visited:
                continue
            if curr_state not in visited:
                visited.add(curr_state)
                for move in moves[idx]:
                    tmp = list(curr_state)
                    tmp[idx], tmp[move] = tmp[move], tmp[idx] # Swap
                    tmp = ''.join(tmp)
                    queue.append((tmp, tmp.index('0'), steps+1))

        return -1

#################################

        moves = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        state = "".join(str(c) for c in board[0] + board[1])
        start = state.index('0')
        visited = set()

        queue = collections.deque([(start, state, 0)])
        while queue:
            cur, state, steps = queue.popleft()
            if state == '123450':
                return steps
            elif state in visited:
                continue
            else:
                visited.add(state)
                for nxt in moves[cur]:
                    tmp = list(state)
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = ''.join(tmp)
                    queue.append((nxt, tmp, steps + 1))
        return -1






        ###
