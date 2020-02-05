#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex: return [1]
        else:
            l = [1, 1]

        for _ in xrange(1, rowIndex):
            l = [l[i] + l[i + 1] for i in xrange(len(l) - 1)]
            l.insert(0, 1)
            l.append(1)

        return l
 
# @lc code=end

