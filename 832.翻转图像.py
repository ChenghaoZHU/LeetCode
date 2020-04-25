#
# @lc app=leetcode.cn id=832 lang=python
#
# [832] 翻转图像
#

# @lc code=start
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def reverse_line(line):
            l, r = 0, len(line) - 1
            while l < r:
                line[l], line[r] = line[r], line[l]
                l += 1
                r -= 1
        
        for l in A:
            reverse_line(l)
            l[:] = [i ^ 1 for i in l]
        return A
        
# @lc code=end

