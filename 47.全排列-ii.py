#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        indexes = range(len(nums))
        def gen_permute(k):
            n = len(indexes)
            tmp = list(indexes)
            p = []
            for i in xrange(1, n + 1):
                b = math.factorial(n - i)
                ch = tmp[k / b]
                tmp.remove(ch)
                p.append(nums[ch])
                k = k % b
            return p

        seen = set()
        res = []
        for i in xrange(math.factorial(len(nums))):
            j = gen_permute(i)
            k = '.'.join(map(str, j))
            if k not in seen:
                seen.add(k)
                res.append(j)
        
        return res
# @lc code=end

