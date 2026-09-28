# 2601. 质数减法运算
'''
给你一个下标从 0 开始的整数数组 nums ，数组长度为 n 。

你可以执行无限次下述运算：

 选择一个之前未选过的下标 i ，并选择一个 严格小于 nums[i] 的质数 p ，从 nums[i] 中减去 p 。

如果你能通过上述运算使得 nums 成为严格递增数组，则返回 true ；否则返回 false 。

严格递增数组 中的每个元素都严格大于其前面的元素。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
