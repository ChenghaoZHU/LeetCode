#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return
        self.rows = len(board)
        self.cols = len(board[0])
        for r in xrange(1, self.rows - 1):
            for c in xrange(1, self.cols - 1):
                self.visited = set()
                self.reset = True
                self.expand(r, c, board)
                self.clear(board)

    def clear(self, board):
        if self.reset:
            while self.visited:
                r, c = self.visited.pop()
                board[r][c] = 'X' 

    def expand(self, r, c, board):
        if r == 0 or c == 0 or r == self.rows - 1 or c == self.cols - 1:
            if board[r][c] == 'O':
                self.reset = False
            return
        if board[r][c] == 'X': return
        self.visited.add((r, c))
        if (r - 1, c) not in self.visited:
            self.expand(r - 1, c, board)
        if (r, c - 1) not in self.visited:
            self.expand(r, c - 1, board)  
        if (r + 1, c) not in self.visited:
            self.expand(r + 1, c, board)
        if (r, c + 1) not in self.visited:
            self.expand(r, c + 1, board)

# @lc code=end

