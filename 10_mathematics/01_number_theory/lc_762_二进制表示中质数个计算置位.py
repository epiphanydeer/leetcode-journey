# 762. 二进制表示中质数个计算置位
'''
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

计算置位位数 就是二进制表示中 1 的个数。

 例如， 21 的二进制表示 10101 有 3 个计算置位。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
