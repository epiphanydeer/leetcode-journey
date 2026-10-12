# 1191. K 次串联后最大子数组之和
'''
给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。

例如，如果 arr = [1, 2] ， k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。

返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。

由于 结果可能会很大，需要返回结果对 109 + 7 取 模。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
