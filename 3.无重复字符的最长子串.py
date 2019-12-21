#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        head = 0
        if not s:  # incase of empty string
            return result
        seen = {s[head]: head}
        
        tail = head + 1
        size = len(s)
        while head <= size:
            while tail < size and s[tail] not in seen:
                seen[s[tail]] = tail
                tail += 1
            candidate = len(seen)
            if candidate > result:
                result = candidate  # temp result
            if tail == size:
                break
            head = seen[s[tail]] + 1
            tail = head + 1
            seen = {s[head]: head}  # clear cache

        return result
# @lc code=end

