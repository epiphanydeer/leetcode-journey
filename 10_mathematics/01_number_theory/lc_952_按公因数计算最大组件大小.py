# 952. 按公因数计算最大组件大小
'''
给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

 有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；

 只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。

返回 图中最大连通组件的大小 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
