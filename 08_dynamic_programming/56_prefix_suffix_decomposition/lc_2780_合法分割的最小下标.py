# 2780. 合法分割的最小下标
'''
如果在长度为 m 的整数数组 arr 中 超过一半 的元素值为 x，那么我们称 x 是 支配元素 。

给你一个下标从 0 开始长度为 n 的整数数组 nums ，数据保证它含有一个 支配 元素。

你需要在下标 i 处将 nums 分割成两个数组 nums[0, ..., i] 和 nums[i + 1, ..., n - 1] ，如果一个分割满足以下条件，我们称它是 合法 的：

 0 <= i < n - 1

 nums[0, ..., i] 和 nums[i + 1, ..., n - 1] 的支配元素相同。

这里， nums[i, ..., j] 表示 nums 的一个子数组，它开始于下标 i ，结束于下标 j ，两个端点都包含在子数组内。特别地，如果 j < i ，那么 nums[i, ..., j] 表示一个空数组。

请你返回一个 合法分割 的 最小 下标。如果合法分割不存在，返回 -1 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
