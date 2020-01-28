#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                break
            digits[i] %= 10
        if digits[0] == 0: digits.insert(0, 1)
        return digits
        
# @lc code=end

