# 1232. 缀点成线
'''
给定一个整数数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。

 

示例 1：

输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

示例 2：

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false

 

提示：

 2 <= coordinates.length <= 1000

 coordinates[i].length == 2

 -104 <= coordinates[i][0], coordinates[i][1] <= 104

 coordinates 中不含重复的点
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
