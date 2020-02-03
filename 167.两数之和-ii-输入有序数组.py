#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)
        while left < right:
            mid = left + (right - left) / 2
            if numbers[mid] == target:
                break
            if numbers[mid] > target:
                right = mid
            elif numbers[mid] < target:
                left = mid + 1
        if left == right or numbers[mid] == target: mid += 1
        seen = {}
        for i in xrange(mid + 1):
            rem = target - numbers[i]
            if rem in seen:
                return [seen[rem] + 1, i + 1]
            seen[numbers[i]] = i
   
# @lc code=end

