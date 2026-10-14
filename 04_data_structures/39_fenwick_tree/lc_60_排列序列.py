# 60. 排列序列
'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

 "123"

 "132"

 "213"

 "231"

 "312"

 "321"

给定 n 和 k，返回第 k 个排列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
