# 2338. 统计理想数组的数目
'''
给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。

对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：

 每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。

 每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。

返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 109 + 7 取余的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
