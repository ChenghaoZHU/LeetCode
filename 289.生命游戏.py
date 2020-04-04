#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def get_live_num(i, j):
            rows = len(board)
            cols = len(board[0])
            neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            n = 0
            for k in neighbours:
                r, c = i + k[0], j + k[1]
                if r < 0 or c < 0 or r == rows or c == cols:
                    continue
                if board[r][c] in (1, 3):
                    n += 1
            return n

        # 3 死去 4 复活
        def updated(i, j):
            n = get_live_num(i, j)
            if board[i][j]:
                if n < 2: return 3
                elif n < 4: return 1
                else: return 3
            else:
                if n == 3: return 4
                return 0

        rows = len(board)
        cols = len(board[0])

        for i in xrange(rows):
            for j in xrange(cols):
                board[i][j] = updated(i, j)

        for i in xrange(rows):
            for j in xrange(cols):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 4:
                    board[i][j] = 1

        
# @lc code=end

