#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        if not (m and n): return matrix
        # matrix[0][0] 很特殊，他要同时表示第0行和第0列
        # 那是不可能的，所有多用一个变量来表示
        reset_col = False
        # 用行首列首记录信息，若matrix[0][1] == 0，表示列1是0
        for i in xrange(m):
            if not matrix[i][0]: reset_col = True
            for j in xrange(1, n):
                if not matrix[i][j]:
                    matrix[0][j] = matrix[i][0] = 0
        
        # set for rows
        for r in xrange(1, m):
            if not matrix[r][0]:
                for c in xrange(n):
                    matrix[r][c] = 0

        # set for cols
        for c in xrange(1, n):
            if not matrix[0][c]:
                for r in xrange(m):
                    matrix[r][c] = 0

        if not matrix[0][0]:
            for c in xrange(1, n):
                matrix[0][c] = 0

        if reset_col:
            for r in xrange(m):
                matrix[r][0] = 0
            
# @lc code=end

