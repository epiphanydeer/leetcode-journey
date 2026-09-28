# 2598. 执行操作后的最大 MEX
'''
给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。

在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。

 例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3] 。

数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。

 例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。

返回在执行上述操作 任意次 后，nums 的最大 MEX 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
