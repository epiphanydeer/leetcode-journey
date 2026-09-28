# 2789. 合并后数组中的最大元素
'''
给你一个下标从 0 开始、由正整数组成的数组 nums 。

你可以在数组上执行下述操作 任意 次：

 选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的下标 i 。将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。

返回你可以从最终数组中获得的 最大 元素的值。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
