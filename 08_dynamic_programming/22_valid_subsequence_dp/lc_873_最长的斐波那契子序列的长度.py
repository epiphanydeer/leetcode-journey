# 873. 最长的斐波那契子序列的长度
'''
如果序列 x1, x2, ..., xn 满足下列条件，就说它是 斐波那契式 的：

 n >= 3

 对于所有 i + 2 <= n，都有 xi + xi+1 == xi+2

给定一个 严格递增 的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果不存在，返回  0 。

子序列 是通过从另一个序列 arr 中删除任意数量的元素（包括删除 0 个元素）得到的，同时不改变剩余元素顺序。例如，[3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的子序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
