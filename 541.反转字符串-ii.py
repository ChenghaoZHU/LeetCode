#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        def rev_str(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        reverse = True
        i, j = 0, k - 1

        while i < len(s):
            if reverse:
                rev_str(i, min(j, len(s) - 1))
            i += k
            j += k
            reverse = not reverse
        return ''.join(s)
# @lc code=end

