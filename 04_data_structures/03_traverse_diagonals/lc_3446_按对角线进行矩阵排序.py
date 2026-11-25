# 3446. 按对角线进行矩阵排序
"""
给你一个大小为 n x n 的整数方阵 grid。返回一个经过如下调整的矩阵：

 左下角三角形（包括中间对角线）的对角线按 非递增顺序 排序。

 右上角三角形 的对角线按 非递减顺序 排序。

"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # 左下三角，i >= j，右下三角 i < j
        n = len(grid)
        diags = defaultdict(list)
        # 1. 按对角线编号 k = i - j 分组收集元素
        for i in range(n):
            for j in range(n):
                diags[i - j].append(grid[i][j])
        # 2. 分别排序（小技巧：排成相反顺序，方便后面用 pop() 从列表末尾 O(1) 弹出）
        for k, vals in diags.items():
            if k >= 0:
                # 左下三角（含主对角线）：题目要从大到小，这里先从小到大排，pop() 就会先吐出最大的
                vals.sort()
            else:
                # 右上三角：题目要从小到大，这里先从大到小排，pop() 就会先吐出最小的
                vals.sort(reverse=True)
        # 3. 再次遍历矩阵，把排好序的数字填回原位
        for i in range(n):
            for j in range(n):
                grid[i][j] = diags[i - j].pop()
        return grid


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
