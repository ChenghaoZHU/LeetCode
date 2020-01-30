#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        M = len(matrix)
        N = len(matrix[0])
        result = []
        flag = True
        for i in xrange(M + N - 1):
            if flag:
                x = min(i, M - 1)
                y = i - x
                while x > -1 and y < N:
                    result.append(matrix[x][y])
                    x -= 1
                    y += 1
            else:
                y = min(i, N - 1)
                x = i - y
                l = M
                while y > -1 and x < M:
                    result.append(matrix[x][y])
                    x += 1
                    y -= 1

            flag = not flag

        return result

# @lc code=end

