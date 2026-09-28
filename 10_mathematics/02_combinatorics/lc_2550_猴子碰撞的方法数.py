# 2550. 猴子碰撞的方法数
'''
现在有一个正凸多边形，其上共有 n 个顶点。顶点按顺时针方向从 0 到 n - 1 依次编号。每个顶点上 正好有一只猴子 。下图中是一个 6 个顶点的凸多边形。

每个猴子同时移动到相邻的顶点。顶点 i 的相邻顶点可以是：

 顺时针方向的顶点 (i + 1) % n ，或

 逆时针方向的顶点 (i - 1 + n) % n 。

如果移动后至少有两只猴子停留在同一个顶点上或者相交在一条边上，则会发生 碰撞 。

返回猴子至少发生 一次碰撞 的移动方法数。由于答案可能非常大，请返回对 109+7 取余后的结果。

注意，每只猴子只能移动一次。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def monkeyMove(self, n):
        """
        :type n: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
