#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        record = None  # 回溯点
        flag = 1  # 可以删除
        while l < r:
            if s[l] != s[r]:
                if flag:
                    if l + 1 < len(s) and s[l + 1] == s[r] and \
                        r - 1 >= 0 and s[r - 1] == s[l]:
                        record = (l, r - 1)
                        l += 1
                        flag -= 1
                        continue
                    elif l + 1 < len(s) and s[l + 1] == s[r]:
                            l += 1
                            flag -= 1
                            continue
                    elif r - 1 >= 0 and s[r - 1] == s[l]:
                            r -= 1
                            flag -= 1
                            continue
                if record:
                    l, r = record  # 回溯
                    record = None
                    continue
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True

# @lc code=end

