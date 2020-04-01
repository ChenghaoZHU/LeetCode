#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        seen = collections.defaultdict(list)
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                seen[nums[i] + nums[j]].append([i, j])

        nums_to_check = set()
        visited = set()
        for n in seen:
            if n in nums_to_check: continue
            nums_to_check.add(n)
            nums_to_check.add(target - n)
            if target -n not in seen: continue
            for i in seen[n]:
                for j in seen[target - n]:
                    candidate = i + j
                    if len(set(candidate)) == 4:
                        candidate = map(nums.__getitem__, candidate)
                        candidate.sort()
                        if tuple(candidate) not in visited:
                            res.append(candidate)
                            visited.add(tuple(candidate))
        
        return res

# @lc code=end

