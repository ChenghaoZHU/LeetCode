#
# @lc app=leetcode.cn id=384 lang=python
#
# [384] 打乱数组
#

# @lc code=start
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.nums[:]
        n = len(nums)
        for i in xrange(n - 1):
            k = random.randint(i, n - 1)
            nums[i], nums[k] = nums[k], nums[i]
        return nums
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

