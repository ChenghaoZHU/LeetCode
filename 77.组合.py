#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        res = []
        def dfs(path, choices, k):
            if len(path) == k:
                res.append(list(path))
                return
            for i, c in enumerate(choices):
                path.append(c)
                dfs(path, choices[i + 1:], k)
                path.pop()

        dfs([], range(1, n + 1), k)
        return res

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 康托逆展开
        def helper(s, k, n):
            tmp = []
            choices = range(1, n + 1)
            for i in xrange(k):
                b = math.factorial(n - i - 1) / math.factorial(n - k)
                idx = s / b
                t = choices.pop(idx)
                if tmp and t < tmp[-1]:
                    return []
                tmp.append(t)
                s = s % b
            return tmp
        res = []
        for i in xrange(math.factorial(n) / math.factorial(n - k)):
            t = helper(i, k, n)
            if t:
                res.append(t)
        return res

# @lc code=end

