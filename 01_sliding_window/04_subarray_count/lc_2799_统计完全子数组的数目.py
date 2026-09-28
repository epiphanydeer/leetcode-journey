# 2799. 统计完全子数组的数目
'''
给你一个由 正 整数组成的数组 nums 。

如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：

 子数组中 不同 元素的数目等于整个数组不同元素的数目。

返回数组中 完全子数组 的数目。

子数组 是数组中的一个连续非空序列。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
