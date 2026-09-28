# 1632. 矩阵转换后的排名
'''
给你一个 m x n 的矩阵 matrix ，请你返回一个新的矩阵 answer ，其中 answer[row][col] 是 matrix[row][col] 的排名。

每个元素的 排名 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：

 排名是从 1 开始的一个整数。

 如果两个元素 p 和 q 在 同一行 或者 同一列 ，那么：
 
 如果 p < q ，那么 rank(p) < rank(q)

 如果 p == q ，那么 rank(p) == rank(q)

 如果 p > q ，那么 rank(p) > rank(q)

 
 

 排名 需要越 小 越好。

题目保证按照上面规则 answer 数组是唯一的。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
