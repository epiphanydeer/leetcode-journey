# 939. 最小面积矩形
'''
给你一个 X-Y 平面上的点数组 points，其中 points[i] = [xi, yi]。

返回由这些点形成的矩形的最小面积，矩形的边与 X 轴和 Y 轴平行。如果不存在这样的矩形，则返回 0。

 

示例 1：

输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
输出： 4

示例 2：

输入： points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出： 2

 

提示：

 1 <= points.length <= 500

 points[i].length == 2

 0 <= xi, yi <= 4 * 104

 所有给定的点都是 唯一 的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
