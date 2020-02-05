#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        sp, fp = 0, 0
        while fp < len(s):
            while fp < len(s) and s[fp] != ' ':
                fp += 1
            self.reverse_str(sp, fp - 1, s)
            fp += 1
            sp = fp
        return ''.join(s)

    def reverse_str(self, sp, fp, s):
        while sp < fp:
            s[sp], s[fp] = s[fp], s[sp]
            sp += 1
            fp -= 1

# @lc code=end

