#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 转置矩阵后翻转行是基本解
        # 下面的解法是旋转外层矩形
        # n % 2是因为n为奇数时，矩边的中点也需要旋转
        n = len(matrix)
        for r in xrange(n / 2 + n % 2):
            for c in xrange(n / 2):
                matrix[r][c], matrix[c][n - 1 - r], \
                matrix[n - 1 - r][n - 1 - c], matrix[n - 1 - c][r] = \
                matrix[n - 1 - c][r], matrix[r][c], \
                matrix[c][n - 1 - r], matrix[n - 1 - r][n - 1 - c]

# @lc code=end
