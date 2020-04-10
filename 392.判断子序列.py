#
# @lc app=leetcode.cn id=392 lang=python
#
# [392] 判断子序列
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cache = collections.defaultdict(collections.deque)
        for i, ch in enumerate(t):
            cache[ch].append(i)
        
        prev = -1
        for ch in s:
            positions = cache[ch]
            valid = False
            while positions:
                i = positions.popleft()  # 不用pop改用二分可适应大数据
                if i > prev:
                    prev = i
                    valid = True
                    break
            if not valid:
                return False
        
        return True

    def isSubsequence_simple(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        i = 0
        for ch in t:
            if ch == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
# @lc code=end

