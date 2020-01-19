#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_values = []
        self.minValue = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if x < self.minValue:
            self.min_values.append(x)
            self.minValue = x
        else:
            self.min_values.append(self.minValue)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.data.pop()
            self.min_values.pop()
            if self.min_values:
                self.minValue = self.min_values[-1]
            else:
                self.minValue = float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1] if self.data else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

