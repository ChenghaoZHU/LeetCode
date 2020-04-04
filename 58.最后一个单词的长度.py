#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        inword = False
        start = -1
        for i, ch in enumerate(s):
            if not inword:
                if ch != ' ':
                    inword = True
                    start = i
            else:
                if ch == ' ':
                    inword = False
                    res = i - start
        if inword: res = i - start + 1
        return res

    def lengthOfLastWord_easy(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if words:
            return len(words[-1])
        return 0
# @lc code=end

