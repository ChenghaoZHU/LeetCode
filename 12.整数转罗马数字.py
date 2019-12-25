#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        base = ['I', 'X', 'C', 'M']
        half = ['V', 'L', 'D']
        i = 0
        while num:
            res = ''
            n = num % 10
            if 1 <= n < 4:
                res = n * base[i]
            elif n == 4:
                res = base[i] + half[i]
            elif n == 5:
                res = half[i]
            elif 6 <= n < 9:
                res = half[i] + (n - 5) * base[i]
            elif n == 9:
                res = base[i] + base[i+1]
            result.append(res)
            i += 1
            num /= 10
        return ''.join(result[::-1])

# @lc code=end

