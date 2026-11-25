# 3623. 统计梯形的数目 I
"""
给你一个二维整数数组 points，其中 points[i] = [xi, yi] 表示第 i 个点在笛卡尔平面上的坐标。

水平梯形 是一种凸四边形，具有 至少一对 水平边（即平行于 x 轴的边）。两条直线平行当且仅当它们的斜率相同。

返回可以从 points 中任意选择四个不同点组成的 水平梯形 数量。

由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。



示例 1：

输入： points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

输出： 3
【解题思路】
1. 两条线平行不相等就可以组成梯形，一条线c个点可以组成c*(c-1)/2条线
2. 使用counter函数计算y轴相等的点，就是一条线存入字典
3. 结果要取模，% 10e9 + 7
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10e9 + 7
        ans = 0
        pre = 0
        cnt = Counter(y for _, y in points)
        for c in cnt.values():
            w = c * (c - 1) // 2
            ans = (ans + w * pre) % MOD
            pre = (w + pre) % MOD
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.countTrapezoids(points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
    print(solution.countTrapezoids(points=[[0, 0], [1, 0], [0, 1], [2, 1]]))
