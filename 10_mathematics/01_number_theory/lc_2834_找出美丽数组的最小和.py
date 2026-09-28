# 2834. 找出美丽数组的最小和
'''
给你两个正整数：n 和 target 。

如果数组 nums 满足下述条件，则称其为 美丽数组 。

 nums.length == n.

 nums 由两两互不相同的正整数组成。

 在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。

返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 109 + 7。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
