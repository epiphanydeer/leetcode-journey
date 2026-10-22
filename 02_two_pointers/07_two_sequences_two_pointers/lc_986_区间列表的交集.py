# 986. 区间列表的交集
"""
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a ）表示实数 x 的集合，而 a 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
【解题思路】
1. 思路简单，AB有交集说明，交集的起点是ab开头数字的最大值，交集的终点是ab末尾的最小数
2. 只要终点减去起点>=0 那就有交集，交集就是这俩数
3. 终点小的数字先走，因为大的可能还会和下一次匹配
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        left, right = 0, 0
        ans = []
        # while 什么时候停止？一方用完的时候
        while left < len(firstList) and right < len(secondList):
            a = max(firstList[left][0], secondList[right][0])
            b = min(firstList[left][1], secondList[right][1])
            if b - a >= 0:
                ans.append([a, b])
            if firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left += 1
            # 边界条件,left，right 一方 = len的时候就中断了

        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.intervalIntersection(
            firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
            secondList=[[1, 5], [8, 12], [15, 24], [25, 26]],
        )
    )
