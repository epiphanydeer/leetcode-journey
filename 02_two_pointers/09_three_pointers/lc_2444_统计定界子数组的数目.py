# 2444. 统计定界子数组的数目
'''
给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

nums 的定界子数组是满足下述条件的一个子数组：

 子数组中的 最小值 等于 minK 。

 子数组中的 最大值 等于 maxK 。

返回定界子数组的数目。

子数组是数组中的一个连续部分。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
