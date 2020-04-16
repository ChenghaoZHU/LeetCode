#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        from itertools import imap
        words = str.split()
        if len(words) != len(pattern):
            return False

        seen = collections.defaultdict(list)
        for i, p in enumerate(pattern):
            seen[p].append(i)
        if len(set(words)) != len(seen):
            return False
        for p in seen:
            if len(set(imap(words.__getitem__, seen[p]))) != 1:
                return False
        return True

# @lc code=end

