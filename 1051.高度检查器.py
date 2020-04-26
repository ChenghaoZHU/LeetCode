#
# @lc app=leetcode.cn id=1051 lang=python
#
# [1051] 高度检查器
#

# @lc code=start
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return len([0 for i, j in zip(heights, sorted(heights)) if i != j])
# @lc code=end

