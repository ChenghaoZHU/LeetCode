#
# @lc app=leetcode.cn id=326 lang=python
#
# [326] 3的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n % 3: return False
        while n > 3:
            temp = math.sqrt(n)
            if str(temp).isdigit():
                n = temp
            else:
                if n % 3: return False
                n /= 3 

        return True if n == 3 else False
        
# @lc code=end

