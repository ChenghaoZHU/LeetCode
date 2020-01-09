#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        for row in board:
            seen = {}
            for i in row:
                if i == '.':
                    continue
                if i in seen:
                    return False
                seen[i] = 1

        for col in xrange(cols):
            seen = {}
            for row in xrange(rows):
                i = board[row][col]
                if i == '.':
                    continue
                if i in seen:
                    return False
                seen[i] = 1
        
        for i in xrange(rows / 3):
            for j in xrange(cols / 3):
               if not self.isValidCell(board, i, j):
                   return False
        
        return True

    def isValidCell(self, board, row, col):
        seen = {}
        for r in xrange(3):
            for c in xrange(3):
                i = board[3 * row + r][3 * col + c]
                if i == '.':
                    continue
                if i in seen:
                    return False
                seen[i] = 1
        return True
# @lc code=end

