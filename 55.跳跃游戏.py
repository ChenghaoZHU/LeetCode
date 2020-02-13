#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0 
        while i < n - 1:
            op = 0
            k = 0
            for j in xrange(1, nums[i] + 1):
                if j + i >= n - 1: return True
                step = j + nums[j + i]
                if step > op:
                    op = step
                    k = j
            if not k: return False
            i += k  # 跳跃
        return True

# @lc code=end

