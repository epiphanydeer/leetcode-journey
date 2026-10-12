# 786. 第 K 个最小的质数分数
'''
给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 质数 组成，且其中所有整数互不相同。

对于每对满足 0 <= i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。

那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
