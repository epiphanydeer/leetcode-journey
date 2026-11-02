# 74. 搜索二维矩阵
"""
给你一个满足下述两条属性的 m x n 整数矩阵：

 每行中的整数从左到右按非严格递增顺序排列。

 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。
【解题思路】
1. 行列这个表达式，m 行 n 列的矩阵a[i] = a[[i//n], [i%n]] i从0开始
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def lower_bound(self, matrix: list[int], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        left = self.lower_bound(matrix, target)
        if left == m * n:
            return False
        return matrix[left // n][left % n] == target


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
        )
    )
    print(
        solution.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
        )
    )
