# 852. 山脉数组的峰顶索引
'''
给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。

返回峰值元素的下标。

你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
