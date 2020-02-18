#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def traceback(w, r, c):
            if (r, c) in visited: return False
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[len(w)]: return False
            
            w += board[r][c]
            visited.add((r, c))
            if w == word: return True
            if traceback(w, r - 1, c): return True
            if traceback(w, r, c + 1): return True
            if traceback(w, r + 1, c): return True
            if traceback(w, r, c - 1): return True

            visited.remove((r, c))

        for i in xrange(rows):
            for j in xrange(cols):
                if traceback('', i, j):
                    return True

        return False
        
# @lc code=end

