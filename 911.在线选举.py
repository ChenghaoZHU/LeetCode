#
# @lc app=leetcode.cn id=911 lang=python
#
# [911] 在线选举
#

# @lc code=start
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times
        self.cache = {}
    
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t in self.cache:
            return self.cache[t]
        counter = collections.Counter()
        tickets = []

        for i, tm in enumerate(self.times):
            if t < tm: break
            tickets.append(self.persons[i])

        counter.update(tickets)
        candidates = set()
        for i in counter.most_common():
            if not candidates:
                candidates.add(i[0])
                best = i[1]
            else:
                if i[1] == best:
                    candidates.add(i[0])
                else:
                    break
        if len(candidates) == 1:
            self.cache[t] = candidates.pop()
            return self.cache[t]
        else:
            i = len(tickets) - 1
            while i >= 0:
                if tickets[i] in candidates:
                    self.cache[t] = tickets[i]
                    return self.cache[t]
                i -= 1
                
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

