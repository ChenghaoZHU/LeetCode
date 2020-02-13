#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 欧拉筛法
        n = n - 1
        _map = [True for _ in xrange(n)]
        count = 0
        primes = []
        for i in xrange(1, n):
            k = i + 1
            if _map[i]:
                primes.append(k)
                count += 1
            for p in primes:
                if p * k > n: break
                _map[p * k - 1] = False
                if k % p == 0: break  # 重点 12 = 4 * 3 or 6 * 2，12应该由6筛去
        return count
# @lc code=end

