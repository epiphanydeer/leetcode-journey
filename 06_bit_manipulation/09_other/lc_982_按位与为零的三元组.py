# 982. 按位与为零的三元组
'''
给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：

 0 <= i < nums.length

 0 <= j < nums.length

 0 <= k < nums.length

 nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
