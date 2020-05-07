#
# @lc app=leetcode.cn id=1095 lang=python
#
# [1095] 山脉数组中查找目标值
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        arr = mountain_arr
        l, r = 0, arr.length() - 1
        # find peak
        while l <= r:
            mid = (l + r) >> 1
            h = arr.get(mid)
            if mid:
                if h > arr.get(mid - 1):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if h < arr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid
                    break
        peak = r
        l, r = 0, peak
        while l <= r:
            mid = (l + r) >> 1
            h = arr.get(mid)
            if h == target:
                return mid
            elif target > h:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = peak + 1, arr.length() - 1
        while l <= r:
            mid = (l + r) >> 1
            h = arr.get(mid)
            if h == target:
                return mid
            elif target < h:
                l = mid + 1
            else:
                r = mid - 1

        return -1
    
# @lc code=end

