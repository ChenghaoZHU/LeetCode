#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.obstacles = set([tuple(ob) for ob in obstacles])
        x, y = 0, 0  # 原点
        d = 'n'  # 默认往北走
        directs = {
            'n-1': 'e',
            'n-2': 'w',
            's-1': 'w',
            's-2': 'e',
            'e-1': 's',
            'e-2': 'n',
            'w-1': 'n',
            'w-2': 's'
        }
        farest = 0
        for cmd in commands:
            if cmd < 0: 
                d = directs['%s%s' % (d, cmd)]  # 转弯
                continue
            if d == 'n':
                y = self.find_obstacle_north(x, y, cmd)
            elif d == 's':
                y = self.find_obstacle_south(x, y, cmd)
            elif d == 'e':
                x = self.find_obstacle_east(x, y, cmd)
            elif d == 'w':
                x = self.find_obstacle_west(x, y, cmd)
            farest = max(farest, x ** 2 + y ** 2)
        
        return farest

    def find_obstacle_west(self, x, y, step):
        if not self.obstacles: return x - step
        for _ in xrange(step):
            if (x - 1, y) not in self.obstacles:
                x -= 1
            else:
                break
        return x

    def find_obstacle_east(self, x, y, step):
        if not self.obstacles: return x + step
        for _ in xrange(step):
            if (x + 1, y) not in self.obstacles:
                x += 1
            else:
                break
        return x

    def find_obstacle_south(self, x, y, step):
        if not self.obstacles: return y - step
        for _ in xrange(step):
            if (x, y - 1) not in self.obstacles:
                y -= 1
            else:
                break
        return y
    
    def find_obstacle_north(self, x, y, step):
        if not self.obstacles: return y + step
        for _ in xrange(step):
            if (x, y + 1) not in self.obstacles:
                y += 1
            else:
                break 
        return y

# @lc code=end

