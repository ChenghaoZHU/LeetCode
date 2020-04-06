#
# @lc app=leetcode.cn id=380 lang=python
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.dict = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = len(self.array)
            self.array.append(val)
            return True
        return False
            
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            idx = self.dict[val]
            self.dict[self.array[-1]] = idx
            self.array[idx], self.array[-1] = self.array[-1], self.array[idx]
            self.array.pop()
            self.dict.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randrange(0, len(self.array))
        return self.array[idx]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

