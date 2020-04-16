#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 if num % 9 or not num else 9
# @lc code=end

