#
# @lc app=leetcode.cn id=1311 lang=python
#
# [1311] 获取你好友已观看的视频
#

# @lc code=start
class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        involved = friends[id]
        visited = set(friends[id])
        visited.add(id)
        
        l = 1
        while l < level:
            temp = []
            while involved:
                i = involved.pop()
                for j in friends[i]:
                    if j not in visited:
                        visited.add(j)
                        temp.append(j)
            involved = temp
            l += 1
        
        from collections import defaultdict
        counter = defaultdict(int)
        for i in involved:
            for j in watchedVideos[i]:
                counter[j] += 1
        
        res = [(counter[k], k) for k in counter]
        res.sort()
        return [i[1] for i in res]

# @lc code=end

