#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, _str):
        """
        :type str: _str
        :rtype: int
        """
        if not _str:
            return 0
        result = ''
        sign = 0
        for i, ch in enumerate(_str):
            if ch == ' ':
                if result or sign:
                    break
            elif ch == '+':
                if result:
                    break
                if not sign:
                    sign = 1
                else:
                    return 0
            elif ch == '-':
                if result:
                    break
                if not sign:
                    sign = -1
                else:
                    return 0
            elif ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                result += ch
            else:
                if result:
                    break
                return 0
        if not result:
            return 0
        result = sign * int(result) if sign else int(result)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
        
# @lc code=end

