#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for l in xrange(1, numRows - 1):
            level = [1]
            last_level = result[l]
            i  = 0
            while i + 1 < len(last_level):
                x = last_level[i] 
                y = last_level[i + 1]
                level.append(x + y)
                i += 1
            level.append(1)
            result.append(level)

        return result
        
# @lc code=end

