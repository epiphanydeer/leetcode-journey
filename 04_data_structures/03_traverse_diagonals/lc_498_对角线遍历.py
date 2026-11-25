# 498. 对角线遍历
"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
【解题思路】
1. 每条对角线上前缀和相等，给每条线k=01排序，k偶数左下往右上走，k奇数反过来
2. 确定列j就确定了i，因k已知 i + j = k
3. k偶数时，j会碰到上边界和右边界，所以j最大值取最小的 i = 0和j=n-1
4. k奇数的时候，j碰到左边界和下边界，j最小值取最大的i = m -1和j=0
"""

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        ans = []
        # i + j = k
        for k in range(m + n - 1):
            minj = max(k - m + 1, 0)
            maxj = min(n - 1, k)
            if k % 2 == 0:
                for j in range(minj, maxj + 1):
                    ans.append(mat[k - j][j])
            else:
                for j in range(maxj, minj - 1, -1):
                    ans.append(mat[k - j][j])
        return ans


# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
