# 2552. 统计上升四元组
'''
给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。

如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：

 0 <= i < j < k < l < n 且

 nums[i] < nums[k] < nums[j] < nums[l] 。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
