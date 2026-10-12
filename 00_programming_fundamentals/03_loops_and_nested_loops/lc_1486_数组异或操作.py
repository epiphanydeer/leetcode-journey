# 1486. 数组异或操作
'''
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
