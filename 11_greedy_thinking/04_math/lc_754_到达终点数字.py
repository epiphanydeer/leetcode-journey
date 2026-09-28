# 754. 到达终点数字
'''
在一根无限长的数轴上，你站在0的位置。终点在target的位置。

你可以做一些数量的移动 numMoves :

 每次你可以选择向左或向右移动。

 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。

给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
