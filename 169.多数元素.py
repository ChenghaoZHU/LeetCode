#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement_hash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n] += 1
            if counter[n] > len(nums) / 2:
                return n
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        cnt = 0
        for n in nums:
            if n == m:
                cnt += 1
            else:
                if cnt: cnt -= 1
                else:
                    m = n
                    cnt = 1
        return m
# @lc code=end

