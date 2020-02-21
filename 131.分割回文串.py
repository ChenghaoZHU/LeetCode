#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.cache = {}

        def traceback(level, temp):
            for t in temp[:-1]:
                if not self.isPalindrome(t):
                    return
            if level == len(s):
                if temp and self.isPalindrome(temp[-1]):
                    res.append(temp)
                return
            
            if not temp:
                traceback(level + 1, [s[0:1]])
                return
            
            traceback(level + 1, temp[:] + [s[level: level + 1]])
            traceback(level + 1, temp[:-1] + [temp[-1] + s[level]])

        traceback(0, [])
        return res

    def isPalindrome(self, word):
        if word in self.cache:
            return self.cache[word]
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                self.cache[word] = False
                return False
            i += 1
            j -= 1
        self.cache[word] = True
        return True

# @lc code=end

