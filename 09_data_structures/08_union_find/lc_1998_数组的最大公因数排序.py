# 1998. 数组的最大公因数排序
'''
给你一个整数数组 nums ，你可以在 nums 上执行下述操作 任意次 ：

 如果 gcd(nums[i], nums[j]) > 1 ，交换 nums[i] 和 nums[j] 的位置。其中 gcd(nums[i], nums[j]) 是 nums[i] 和 nums[j] 的最大公因数。

如果能使用上述交换方式将 nums 按 非递减顺序 排列，返回 true ；否则，返回 false 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
