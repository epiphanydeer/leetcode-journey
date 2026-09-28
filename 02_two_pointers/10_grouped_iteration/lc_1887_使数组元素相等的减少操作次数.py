# 1887. 使数组元素相等的减少操作次数
'''
给你一个整数数组 nums ，你的目标是令 nums 中的所有元素相等。完成一次减少操作需要遵照下面的几个步骤：

 找出 nums 中的 最大 值。记这个值为 largest 并取其下标 i （下标从 0 开始计数）。如果有多个元素都是最大值，则取最小的 i 。

 找出 nums 中的 下一个最大 值，这个值 严格小于 largest ，记为 nextLargest 。

 将 nums[i] 减少到 nextLargest 。

返回使 nums 中的所有元素相等的操作次数。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
