#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 最小缺失正整数肯定小于等于size + 1
        found = False
        size = len(nums)
        for i, n in enumerate(nums):
            if n == 1:
                found = True
            elif n <= 0 or n > size:
                nums[i] = 1
        if not found:
            return 1
        # 利用数组做hash效果
        # index是key，value是负数表示出现过
        # size用0表示
        for i, n in enumerate(nums):
            n = abs(n)
            if n == size and nums[0] > 0:
                nums[0] = -nums[0]
            elif n < size and nums[n] > 0:
                nums[n] = -nums[n]
        
        # element 0 for n, which equals to size
        for i, n in enumerate(nums[1:], 1):
            if n > 0:
                return i
        return size if nums[0] > 0 else size + 1

# @lc code=end

