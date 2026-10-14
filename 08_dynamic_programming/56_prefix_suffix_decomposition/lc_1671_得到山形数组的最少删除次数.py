# 1671. 得到山形数组的最少删除次数
'''
我们定义 arr 是 山形数组 当且仅当它满足：

 arr.length >= 3

 存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
 
 arr[0] < arr[1] < ... < arr[i - 1] < arr[i]

 arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 
 

给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
