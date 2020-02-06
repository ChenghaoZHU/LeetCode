#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # sort in-place to save storage
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0 
        result = []  # merge
        while p1 < len(nums1) and p2 < len(nums2):
            a, b = nums1[p1], nums2[p2]
            if a == b:
                result.append(a)
                p1 += 1
                p2 += 1
            elif a > b:
                p2 += 1
            else:
                p1 += 1
        return result

# @lc code=end

