#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        label = ''
        while n:
            if n % 26:
                label += chr(ord('A') - 1 + n % 26)
                n /= 26
            else:
                label += 'Z'
                n /= 26
                n -= 1
        return label[::-1]
# @lc code=end

