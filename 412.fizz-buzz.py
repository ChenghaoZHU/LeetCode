#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(n):
            i += 1
            s = ''
            if i % 3 == 0: 
                s += 'Fizz'
            if i % 5 == 0: 
                s += 'Buzz'
            if s:
                result.append(s)
            else:
                result.append(str(i))
            
        return result
# @lc code=end

